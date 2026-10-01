# Motion

Which target accounts should sales and marketing work this week, and what is the play for each?

Inputs: `field/target-accounts.csv`, `field/signals.csv` (copy the template if it is missing), and `field/ledger.csv` if it exists.

## Watch

For each account and each signal, fill the query: `{account}` is the account, `{competitors}` comes from `company.md`, `{team}` is the team that would use the product. Run `search "<query>" --since <today minus window_days> --num 5`.

Keep a result only if the page text shows the signal for that account. Append each kept result to `field/signal-log.csv`:

`date_found,account,signal,weight,published,title,url,person_named`

Do not add a URL that is already in the log for the same account.

## Score

Score is arithmetic only, so the same log and date give the same result.

- Each signal scores `weight × (1 − age_days / window_days)`. Signals older than their window score 0.
- Add 3 for each event in `ledger.csv` the account attended in the last 90 days.
- An account is **in motion** when its score is 8 or more and its newest signal is 60 days old or less.

## Output

`field/out/motion-<date>.md`:

1. **In motion.** One block per account: score, the dated evidence with sources, the people named by the sources, one play, one owner. Take the owner from `target-accounts.csv`.
2. **Plays.** Pick one per account: an invitation to the next event in the plan, a seat at a dinner, a direct note from the owner with the signal as the reason, or hold while an open opportunity belongs to sales.
3. **Movement.** Accounts that entered or left motion since the last report in `field/out/`.
4. **Count.** Accounts watched, signals found, accounts in motion.
5. **Gaps.**
