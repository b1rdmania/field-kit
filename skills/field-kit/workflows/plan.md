# Event plan

A 13-week event plan for one region. This is the default workflow.

## Steps

1. If `field/brief.md` does not exist, run `brief.md` and wait for the user's answers before step 2. If the user explicitly requests a draft on assumptions, follow the exception in `brief.md`.
2. Run `competitors.md`.
3. If `field/target-accounts.csv` is empty, run `accounts.md` in Build mode, including its Review step. If it has fewer than 15 accounts, say so under Risks and continue.
4. Run `events.md`, so it can mark the target accounts.
5. Write the plan.

## The plan

`field/out/plan-<region>-<date>.md`, 600 words at most outside the tables. Week 1 starts next Monday.

1. **The problem.** From the brief, in two lines, and the fix this plan applies.
2. **Goal.** What a win is, from the brief, as numbers for 13 weeks. If the user gave no numbers, propose them and mark them as proposals. Pipeline needs a contract value from the brief. If there is none, give meetings and opportunities only.
3. **What competitors are doing.** Three lines from the competitors output, and what the plan does about it.
4. **Calendar.** Weeks 1 to 13. Each row: week, event or format, city, why, companies it could reach, cost, owner. Mix large events where buyers already go, small rooms the team runs (dinners, demo nights) and co-hosted meetups. Take costs from the brief or a source. Mark any other cost "estimate". Weeks 1 to 4 also hold the setup: agree what counts as a win with sales, start the ledger from `templates/ledger.csv`, book the first small room. From week 9, compare events in `ledger.csv`, cut the format with the worst cost per company reached, and repeat the best.
5. **Budget and measures.** Spend by format against the budget. Measures: invited, attended, target companies attended, meetings, opportunities, pipeline. Say which come from the ledger and which from the sales system.
6. **Risks.**

Link to the competitors, events and accounts outputs for detail. Once the plan starts, run `ledger.md` after each event and `motion.md` weekly.
