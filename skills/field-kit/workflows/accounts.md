# Accounts

Create or check the target account list. Every other workflow reads `field/target-accounts.csv`, so this workflow runs first.

Three ways in. Ask the user which one fits if they do not say:

| The user has | Mode |
| --- | --- |
| A target list, pasted or as a CSV | **Feed** |
| Customers or a few example accounts, and wants more like them | **Mirror** |
| Nothing yet | **Build** |

All three modes end with the same review step. Do not write `target-accounts.csv` until the user approves the list.

## Feed

1. Read the list. Accept any columns. Map them to `account,domain,owner,status,tier,notes`.
2. Remove duplicates by domain, then by name.
3. For each account with no domain, run `search "<account>" --category company --num 1` and take the domain from the result. Mark the domain "unconfirmed" if no result matches.
4. Propose a tier for each account with no tier. Tier 1 fits "Who buys" in `company.md` best. Give one short reason per tier 1 account.
5. Do not change an owner or status the user gave.

If the list has fewer than 20 accounts, offer Mirror mode with the list as seeds.

## Mirror

Seeds are the customers under "Customers we can name" in `company.md`, the accounts already in `field/target-accounts.csv`, or examples the user names. Ask for the region if `company.md` does not give one.

For each seed:

1. `search "<what the seed does>, company headquartered in <region>" --category company --num 10`
2. `search "<region> startup building <what the seed does> raises funding round" --since <one year ago> --num 6`
3. Find the seed's homepage, then `similar <homepage> --num 10`.
4. One `answer`: "Which <region> companies are the best-known equivalents of <seed> (<what it does>)? Name the companies, their cities and their latest funding."

## Build

Use "What we sell", "Who buys" and "Region" from `company.md`. If "Who buys" is vague, ask the user for two or three company types before you search.

For each company type:

1. `search "<company type> company headquartered in <region>" --category company --num 15`
2. `search "<region> <company type> raises funding round" --since <one year ago> --num 10`
3. `answer "Which are the leading <company type> companies in <region>? Name the companies, their cities and their latest funding."`

Then take the three strongest results and run Mirror mode on them to fill the list.

## Rules for Mirror and Build

- Drop directories, listicles, media, consultancies, the seeds themselves and duplicates by domain.
- A company must have its headquarters or a real office in the region.
- A company must show activity in the last 18 months in the source: funding, a launch, open roles or a dated post.
- The city must come from the source. Write "unconfirmed" if it does not.
- Companies with named funding, named customers or a known product go first.
- At most 30 new accounts per run.
- Mark any company already in `target-accounts.csv` as "on list".

## Review

Show the user the list as a table: Account | Domain | City | Tier | Why | On list | Source. Then ask them to:

1. Remove accounts that are wrong, competitors, or off limits.
2. Confirm or change tiers.
3. Add owners, or leave them blank.

Write the approved list to `field/target-accounts.csv`. New accounts get status "new" unless the user gives one. Never remove or overwrite an existing row without the user's approval.

## Output

For Mirror and Build, also write `field/out/accounts-<region>-<date>.md`:

1. **Accounts found.** The review table.
2. **Clusters.** Table: City | Accounts | Main type | Read. Then two or three sentences on which city to start in and which event format fits each cluster.
3. **Where the list breaks.** Seed or company types with no match in the region. Clusters in the region with no seed precedent. Mark inference as inference.
4. **Gaps.**
