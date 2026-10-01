# 90-day plan

A field plan for one region over 90 days. It runs the other workflows, then joins their results into one plan.

Before you start, `field/company.md` must be filled and `field/target-accounts.csv` must have accounts. If there are fewer than 20 target accounts, run `mirror.md` in expand mode first and ask the user which results to add.

## Steps

1. `events.md` for the region.
2. `cohosts.md` for the one or two cities with the most target accounts.
3. `motion.md` for a first read of which accounts are warm now.
4. Write the plan.

## The plan

`field/out/plan-<region>-<date>.md`:

1. **Goal.** What a win is, from `company.md`, as numbers for 90 days. If the user has no numbers, propose them and mark them as proposals.
2. **Accounts.** The target accounts by tier, with the accounts in motion first.
3. **Calendar.** Weeks 1 to 13. Each row: week, event or format, city, which target accounts it reaches, cost, owner. Use a mix: one or two large events where target accounts already go, small rooms the team runs itself (dinners, demo nights) and co-hosted rooms.
4. **First 30 days.** Definitions agreed with sales, the ledger set up, the first small room booked, the first motion report sent.
5. **Days 31 to 60.** The first events run and logged. Plays sent from the weekly motion report.
6. **Days 61 to 90.** Compare events in `ledger.csv`. Cut the formats with the worst cost per target account attended. Repeat the best.
7. **Budget.** Spend by format against the budget in `company.md`.
8. **Measures.** Invited, attended, target accounts attended, meetings, opportunities, pipeline. Say which come from the ledger and which come from the sales system.
9. **Risks and gaps.**

Keep the plan to two pages. Link to the workflow outputs for detail.
