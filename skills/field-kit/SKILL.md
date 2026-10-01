---
name: field-kit
description: Plan and run event-led pipeline for a B2B team. Builds a 90-day field plan, mirrors target accounts and customers into a region, maps competitor events and the gaps, finds co-hosts, turns a guest list into a pipeline ledger, and says which target accounts to work this week. Use when the user asks for a field marketing plan, event strategy, "which events should we do", account-based events, a lookalike account list for a region, an event ROI ledger, or "which accounts are in motion".
---

# field-kit

Event-led pipeline for B2B teams. Every workflow starts from the team's target accounts. An event is a way to reach those accounts, not the goal.

## Setup

All work lives in a `field/` folder in the user's working directory.

1. If `field/` does not exist, create it and copy the files from `templates/` into it.
2. Ask the user to fill `field/company.md` first. Ask the questions in that file one at a time if the user prefers. Do not start a workflow with an empty `company.md`.
3. Ask for the target account list. The user can paste it, give a CSV, or ask you to build one with the mirror workflow. Save it as `field/target-accounts.csv`.
4. Read `field/company.md` and `field/target-accounts.csv` at the start of every workflow.

## Search

Run `scripts/search.py` (in this skill's folder) for all web research. It uses Exa when `EXA_API_KEY` is set and Perplexity when `PERPLEXITY_API_KEY` is set.

```bash
python3 scripts/search.py search "query" --num 10 --since 2026-01-01 --category company
python3 scripts/search.py similar https://example.com --num 10
python3 scripts/search.py answer "question"
```

If the script exits with code 2, no key is set. Tell the user once: "field-kit works best with an Exa API key (exa.ai). Set EXA_API_KEY in your environment or in a .env file in this folder. I will use my own web search until then." Then use the host's web search tool for the rest of the run. Do not repeat the message.

`--category company` and `similar` work best with Exa. With other providers, check that each result is a company page.

## Workflows

Read the workflow file before you start it.

| User asks | Workflow |
| --- | --- |
| A 90-day plan, a field strategy, where to start | `workflows/plan.md` |
| Companies in a region that look like our customers or targets | `workflows/mirror.md` |
| Which events competitors run, which events to attend or sponsor | `workflows/events.md` |
| Who already runs the room for an audience in a city | `workflows/cohosts.md` |
| A guest list or attendee export, event ROI, a ledger | `workflows/ledger.md` |
| Which accounts to work this week, account signals | `workflows/motion.md` |

`plan.md` runs the others in order. Each workflow also runs alone.

## Rules for every output

- Write to `field/out/` as markdown, one file per run, named `<workflow>-<subject>-<date>.md`. Ledgers are CSV.
- Every fact has a source URL. If the research did not find it, say so. Do not fill gaps from memory.
- Mark each target account that appears in a result. The target account match is the most important column in every table.
- Companies first. Name a person only when a public source names them in that role, and give the source.
- Plain English. Sentences of 20 words or fewer. Active voice. Tables over prose.
- End every output with a short "Gaps" section: what the research could not establish and what a person checks next.
- Never contact anyone. Draft messages only when the user asks, and never send them.
