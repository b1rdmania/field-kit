# field-kit

Event-led pipeline for B2B teams. A skill for Claude, ChatGPT and Codex.

field-kit starts from the team's target accounts. It finds the events, rooms and co-hosts that reach those accounts, logs each event against the list, and says which accounts to work each week. It does not contact anyone.

## What it does

| Ask | Output |
| --- | --- |
| "Write a 90-day field plan for London" | A two-page plan: goal, accounts by tier, a 13-week calendar, budget, measures |
| "Find companies in Europe like our customers" | Lookalike accounts by city, with the source for each, marked against the target list |
| "Which events do our competitors run?" | Competitor events, the region's calendar, which target accounts attend, and the gap |
| "Who runs AI developer meetups in Berlin?" | Recurring rooms, who runs them, size, last date seen |
| "Log last night's demo night" (with a guest export) | An attendee sheet and one row in a ledger of every event |
| "Which accounts are in motion this week?" | Accounts with dated signals, a score, one play and one owner each |

## Search

Research uses [Exa](https://exa.ai). Bring your own key: set `EXA_API_KEY` in the environment or in a `.env` file in the working folder. If no Exa key is set, field-kit uses `PERPLEXITY_API_KEY`, then the host's own web search. Exa gives the best results for company search and lookalikes.

## Install

Claude Code:

```
/plugin marketplace add b1rdmania/field-kit
/plugin install field-kit@field-kit
```

Codex CLI:

```
codex plugin marketplace add b1rdmania/field-kit
```

Claude.ai or ChatGPT: upload the `skills/field-kit` folder as a skill. The search script does not run there, so the skill uses the host's web search.

## Use

Ask for any row in the table. On the first run, field-kit creates a `field/` folder and asks for two things:

1. `field/company.md`: what you sell, who buys, competitors, region, budget, what a win is.
2. `field/target-accounts.csv`: your target accounts. If you have none, ask for a mirror of your customers.

All output goes to `field/out/`. Git ignores `field/`, because guest lists contain personal data.

`examples/larkspur/` has a filled `company.md` and target list for a made-up company.

## Licence

MIT
