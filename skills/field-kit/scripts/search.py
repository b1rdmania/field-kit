#!/usr/bin/env python3
"""Web search for field-kit. Exa first, Perplexity second.

Commands:
  search "query" [--num 10] [--since 2026-01-01] [--category company]
  answer "question"
  fetch https://example.com/sponsors [--chars 40000]

Keys come from EXA_API_KEY or PERPLEXITY_API_KEY, in the environment or in
a .env file in the working folder. Output is JSON on stdout:
  {"provider": "exa", "results": [{"title", "url", "published", "text"}]}

With Exa, answer returns one result: {"answer", "citations": [rows]}.
Fetch returns the page text in "text". It needs Exa.

If Exa fails, search and answer try Perplexity. Exit code 2 means no
provider worked: no key, a failed call, curl missing, or a command that
needs Exa. The caller then uses its own web search or fetch.
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


class SearchError(Exception):
    pass


def load_keys():
    keys = {k: os.environ.get(k) for k in ("EXA_API_KEY", "PERPLEXITY_API_KEY")}
    env = pathlib.Path.cwd() / ".env"
    if env.exists():
        for line in env.read_text().splitlines():
            name, _, value = line.strip().removeprefix("export ").partition("=")
            name = name.strip()
            if name in keys and not keys[name]:
                keys[name] = value.strip().strip("\"'")
    return keys


def post(url, headers, body):
    # curl, not urllib: some Python installs ship without SSL certificates.
    cmd = ["curl", "-s", "--fail-with-body", "-X", "POST", url,
           "-H", "Content-Type: application/json", "-d", json.dumps(body)]
    for h in headers:
        cmd += ["-H", h]
    try:
        r = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
    except FileNotFoundError:
        raise SearchError("curl is not installed")
    except subprocess.TimeoutExpired:
        raise SearchError("timed out after 120 seconds")
    if r.returncode != 0:
        raise SearchError((r.stdout or r.stderr)[:300])
    try:
        return json.loads(r.stdout)
    except json.JSONDecodeError:
        raise SearchError("response was not JSON")


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


# Each command returns its attempts in order: (provider, key name, call).


def cmd_search(a):
    def exa_call(key):
        body = {"query": a.query, "numResults": a.num,
                "contents": {"text": {"maxCharacters": 1200}}}
        if a.category:
            body["category"] = a.category
        if a.since:
            body["startPublishedDate"] = a.since
        return exa_rows(exa(key, "/search", body)["results"])
    # Perplexity ignores --since and --category. Check dates in the results.
    return [("exa", "EXA_API_KEY", exa_call),
            ("perplexity", "PERPLEXITY_API_KEY",
             lambda key: perplexity_search(key, a.query, a.num))]


def cmd_answer(a):
    def exa_call(key):
        out = exa(key, "/answer", {"query": a.question, "text": False})
        rows = [{"title": c.get("title"), "url": c.get("url"), "published": None,
                 "text": ""} for c in out.get("citations", [])[:5]]
        return [{"answer": out.get("answer", ""), "citations": rows}]
    return [("exa", "EXA_API_KEY", exa_call),
            ("perplexity", "PERPLEXITY_API_KEY",
             lambda key: perplexity_search(key, a.question, 8))]


def cmd_fetch(a):
    def exa_call(key):
        out = exa(key, "/contents", {"urls": [a.url], "text": {"maxCharacters": a.chars}})
        return [{"title": r.get("title"), "url": r.get("url"),
                 "published": r.get("publishedDate"), "text": r.get("text") or ""}
                for r in out.get("results", [])]
    return [("exa", "EXA_API_KEY", exa_call)]


def main():
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    sub = p.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser("search")
    s.add_argument("query")
    s.add_argument("--num", type=int, default=10)
    s.add_argument("--since")
    s.add_argument("--category", help="Exa only: company, news, research paper")
    s.set_defaults(fn=cmd_search)
    q = sub.add_parser("answer")
    q.add_argument("question")
    q.set_defaults(fn=cmd_answer)
    f = sub.add_parser("fetch")
    f.add_argument("url")
    f.add_argument("--chars", type=int, default=40000)
    f.set_defaults(fn=cmd_fetch)
    a = p.parse_args()

    keys = load_keys()
    errors = []
    for provider, key_name, call in a.fn(a):
        if not keys[key_name]:
            continue
        try:
            results = call(keys[key_name])
        except SearchError as e:
            errors.append(f"{provider}: {e}")
            continue
        json.dump({"provider": provider, "results": results}, sys.stdout, indent=1)
        print()
        return
    if errors:
        print("Search failed. " + " | ".join(errors), file=sys.stderr)
    elif a.cmd == "fetch":
        print("fetch needs EXA_API_KEY.", file=sys.stderr)
    else:
        print("No search key. Set EXA_API_KEY (preferred) or PERPLEXITY_API_KEY.",
              file=sys.stderr)
    print("Use the host's own web search and fetch tools.", file=sys.stderr)
    sys.exit(NO_KEY)


if __name__ == "__main__":
    main()
