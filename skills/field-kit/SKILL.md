---
name: field-kit
description: Plan and run event-led pipeline for a B2B team. Creates or checks the target account list (feed, mirror or build), builds a 90-day field plan, maps the conferences, competitor events and meetups that reach those accounts, turns a guest list into a pipeline ledger, and says which target accounts to work this week. Use when the user asks for a field marketing plan, event strategy, "which events should we do", account-based events, a lookalike account list for a region, an event ROI ledger, or "which accounts are in motion". Research uses Exa, then Perplexity, then the host's own web search.
---

# field-kit

Event-led pipeline for B2B teams. Every workflow starts from the team's target accounts. An event is a way to reach those accounts, not the goal.

## Setup

All work lives in a `field/` folder in the user's working directory.

1. If `field/` does not exist, create it and copy `templates/` into it.
2. Ask the user to fill `field/company.md`, one question at a time if they prefer. No workflow starts with it empty.
3. Run `workflows/accounts.md`. No other workflow runs until `field/target-accounts.csv` has approved accounts.
4. Read `company.md` and `target-accounts.csv` at the start of every workflow.

## Search

Run `scripts/search.py` (in this skill's folder) for all web research. It uses Exa when `EXA_API_KEY` is set, else Perplexity when `PERPLEXITY_API_KEY` is set.

```bash
python3 scripts/search.py search "query" --num 10 --since 2026-01-01 --category company
python3 scripts/search.py answer "question"
python3 scripts/search.py fetch https://example.com/sponsors
```

Search results hold only part of each page. Use `fetch` to read a full page, such as a speaker list. It returns up to 40,000 characters. `--chars` sets more.

If the script exits with code 2, the key it needs is not set. Tell the user once: "field-kit works best with an Exa API key (exa.ai). Set EXA_API_KEY in your environment or in a .env file in this folder. I will use my own web search until then." Then use the host's own search and fetch tools for the rest of the run. Do not repeat the message. Without Exa, check that each `--category company` result is a company page.

**Region.** Before any search, split the region into three to five cities with the most likely buyers, or countries for a large region. Search each on its own. "London and Western Europe" as one query returns noise.

## Workflows

Read the workflow file before you start it.

| User asks | Workflow |
| --- | --- |
| A 90-day plan, a field strategy, where to start | `workflows/plan.md` |
| A target list, more accounts, lookalikes of our customers | `workflows/accounts.md` |
| Which events to attend or sponsor, what competitors run, who runs meetups in a city | `workflows/events.md` |
| A guest list or attendee export, event ROI, a ledger | `workflows/ledger.md` |
| Which accounts to work this week, account signals | `workflows/motion.md` |

`accounts.md` runs first. `plan.md` runs `events.md`, then writes the plan. Each workflow also runs alone.

## Rules for every output

- Write to `field/out/` as markdown, one file per run, named `<workflow>-<subject>-<date>.md`. Ledgers are CSV.
- Every fact has a source URL. If the research did not find it, say so. Do not fill gaps from memory.
- Use `answer` to find names. Take every fact from a search result or a fetched page, never from answer text.
- Never state anything listed under "What not to claim" in `company.md`.
- Mark each target account that appears in a result. It is the most important column in every table. A match needs the whole name used for the company, as in "at Lloyds" or a sponsor list. A common word ("Tomorro" in "tomorrow"), a namesake or a past employer is not a match. If unsure, write "possible" and quote the line.
- Companies first. Name a person only when a public source names them in that role, and give the source.
- Plain English. Sentences of 20 words or fewer. Active voice. Tables over prose.
- End every markdown output with a short "Gaps" section: what the research could not establish and what a person checks next.
- Never contact anyone. Draft messages only when the user asks, and never send them.
