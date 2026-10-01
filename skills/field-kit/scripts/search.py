#!/usr/bin/env python3
"""Web search for field-kit. Exa first, Perplexity second.

Commands:
  search "query" [--num 10] [--since 2026-01-01] [--category company]
  similar https://example.com [--num 10]
  answer "question"
  fetch https://example.com/sponsors [--chars 8000]

Keys come from EXA_API_KEY or PERPLEXITY_API_KEY, in the environment or in
a .env file in the working folder. Output is JSON on stdout:
  {"provider": "exa", "results": [{"title", "url", "published", "text"}]}

With Exa, answer returns one result: {"answer", "citations": [rows]}.
Fetch returns the page text in "text". It needs Exa.

Exit code 2 means no key is set, or the command needs Exa and only
Perplexity is set. The caller then uses its own web search or fetch.
"""

import argparse
import json
import os
import pathlib
import subprocess
import sys

EXA = "https://api.exa.ai"
PERPLEXITY = "https://api.perplexity.ai"
NO_KEY = 2


def load_keys():
    keys = {k: os.environ.get(k) for k in ("EXA_API_KEY", "PERPLEXITY_API_KEY")}
    env = pathlib.Path.cwd() / ".env"
    if env.exists():
        for line in env.read_text().splitlines():
            name, _, value = line.partition("=")
            if name.strip() in keys and not keys[name.strip()]:
                keys[name.strip()] = value.strip().strip('"')
    return keys


def post(url, headers, body):
    # curl, not urllib: some Python installs ship without SSL certificates.
    cmd = ["curl", "-s", "--fail-with-body", "-X", "POST", url,
           "-H", "Content-Type: application/json", "-d", json.dumps(body)]
    for h in headers:
        cmd += ["-H", h]
    r = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
    if r.returncode != 0:
        sys.exit(f"search failed: {(r.stdout or r.stderr)[:300]}")
    return json.loads(r.stdout)


def exa(key, path, body):
    return post(EXA + path, [f"x-api-key: {key}"], body)


def exa_rows(results):
    return [{"title": r.get("title"), "url": r.get("url"),
             "published": r.get("publishedDate"),
             "text": (r.get("text") or "")[:1200]} for r in results]


def perplexity_search(key, query, num):
    out = post(PERPLEXITY + "/search", [f"Authorization: Bearer {key}"],
               {"query": query, "max_results": min(num, 20)})
    return [{"title": r.get("title"), "url": r.get("url"),
             "published": r.get("date"), "text": (r.get("snippet") or "")[:1200]}
            for r in out.get("results", [])]


def cmd_search(keys, a):
    if keys["EXA_API_KEY"]:
        body = {"query": a.query, "numResults": a.num,
                "contents": {"text": {"maxCharacters": 1200}}}
        if a.category:
            body["category"] = a.category
        if a.since:
            body["startPublishedDate"] = a.since
        return "exa", exa_rows(exa(keys["EXA_API_KEY"], "/search", body)["results"])
    # Perplexity ignores --since and --category. Check dates in the results.
    return "perplexity", perplexity_search(keys["PERPLEXITY_API_KEY"], a.query, a.num)


def cmd_similar(keys, a):
    if keys["EXA_API_KEY"]:
        body = {"url": a.url, "numResults": a.num, "excludeSourceDomain": True,
                "contents": {"text": {"maxCharacters": 600}}}
        return "exa", exa_rows(exa(keys["EXA_API_KEY"], "/findSimilar", body)["results"])
    return "perplexity", perplexity_search(
        keys["PERPLEXITY_API_KEY"], f"companies similar to {a.url}", a.num)


def cmd_answer(keys, a):
    if keys["EXA_API_KEY"]:
        out = exa(keys["EXA_API_KEY"], "/answer", {"query": a.question, "text": False})
        rows = [{"title": c.get("title"), "url": c.get("url"), "published": None,
                 "text": ""} for c in out.get("citations", [])[:5]]
        return "exa", [{"answer": out.get("answer", ""), "citations": rows}]
    return "perplexity", perplexity_search(keys["PERPLEXITY_API_KEY"], a.question, 8)


def cmd_fetch(keys, a):
    if not keys["EXA_API_KEY"]:
        print("fetch needs EXA_API_KEY. Use the host's own fetch tool.", file=sys.stderr)
        sys.exit(NO_KEY)
    out = exa(keys["EXA_API_KEY"], "/contents",
              {"urls": [a.url], "text": {"maxCharacters": a.chars}})
    return "exa", [{"title": r.get("title"), "url": r.get("url"),
                    "published": r.get("publishedDate"), "text": r.get("text") or ""}
                   for r in out.get("results", [])]


def main():
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    sub = p.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser("search")
    s.add_argument("query")
    s.add_argument("--num", type=int, default=10)
    s.add_argument("--since")
    s.add_argument("--category", help="Exa only: company, news, research paper")
    s.set_defaults(fn=cmd_search)
    m = sub.add_parser("similar")
    m.add_argument("url")
    m.add_argument("--num", type=int, default=10)
    m.set_defaults(fn=cmd_similar)
    q = sub.add_parser("answer")
    q.add_argument("question")
    q.set_defaults(fn=cmd_answer)
    f = sub.add_parser("fetch")
    f.add_argument("url")
    f.add_argument("--chars", type=int, default=8000)
    f.set_defaults(fn=cmd_fetch)
    a = p.parse_args()

    keys = load_keys()
    if not any(keys.values()):
        print("No search key. Set EXA_API_KEY (preferred) or PERPLEXITY_API_KEY. "
              "Until then, use the host's own web search.", file=sys.stderr)
        sys.exit(NO_KEY)
    provider, results = a.fn(keys, a)
    json.dump({"provider": provider, "results": results}, sys.stdout, indent=1)
    print()


if __name__ == "__main__":
    main()
