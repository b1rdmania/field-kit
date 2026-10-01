# Motion

Which target accounts should sales and marketing work this week, and what is the play for each? Run it weekly, on tier 1 accounts first.

Inputs: `field/target-accounts.csv`, `field/signals.csv` (copy it from `templates/` if it is missing), and `field/ledger.csv` if it exists.

## Watch

For each account and each signal, fill the query: `{account}` is the account, `{competitors}` comes from `company.md`, `{team}` is the team that would use the product. Run `search "<query>" --since <90 days ago> --num 5`.

Keep a result only if the page text shows the signal for that account. Append each kept result to `field/signal-log.csv`:

`date_found,account,signal,published,title,url,person_named`

Do not add a URL that is already in the log for the same account.

## In motion

An account is in motion when, in the last 60 days, it has:

- two or more signals, or
- one signal and attendance at an event in `ledger.csv`.

## Output

`field/out/motion-<date>.md`:

1. **In motion.** One block per account: the dated evidence with sources, the people named by the sources, one play and one owner. Take the owner from `target-accounts.csv`. The play is one of: an invitation to the next event in the plan, a seat at a dinner, a direct note from the owner with the signal as the reason, or hold while sales owns an open opportunity.
2. **Movement.** Accounts that entered or left motion since the last report in `field/out/`.
3. **Count.** Accounts watched, signals found, accounts in motion.
