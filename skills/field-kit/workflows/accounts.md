# Accounts

Create or check the target account list. Every other workflow reads `field/target-accounts.csv`, so this workflow runs first.

Three ways in. Ask the user which one fits if they do not say:

| The user has | Mode |
| --- | --- |
| A target list, pasted or as a CSV | **Feed** |
| Customers or a few example accounts, and wants more like them | **Mirror** |
| Nothing yet | **Build** |

All three modes end with the domain check and the review. Do not write `target-accounts.csv` until the user approves the list.

## Feed

1. Read the list. Accept any columns. Map them to `account,domain,owner,status,tier,notes`.
2. Remove duplicates by domain, then by name.
3. Propose a tier for each account with no tier. Tier 1 fits "Who buys" in `company.md` best. Give one short reason per tier 1 account.
4. Do not change an owner or status the user gave.

If the list has fewer than 20 accounts, offer Mirror mode with the list as seeds.

## Mirror

Seeds are the customers under "Customers we can name" in `company.md`, accounts already in `field/target-accounts.csv`, or examples the user names. A seed is a company that buys, or would buy, what the user sells. It is never a vendor of a similar product. Seeds stay on the list.

For each seed and each city in the region:

1. `search "<what the seed does>, company headquartered in <city>" --category company --num 10`
2. `search "<city> startup building <what the seed does> raises funding round" --since <one year ago> --num 6`

Then one `answer` per seed: "Which <region> companies are the best-known equivalents of <seed> (<what it does>)? Name the companies, their cities and their latest funding."

## Build

Aim for 20 to 30 approved accounts.

Use "What we sell", "Who buys" and "Region" from `company.md`. Turn "Who buys" into two or three concrete company types. A concrete type names a product and a buyer, for example "contract review software for law firms". "AI-native software company" is too broad. If you cannot make the types concrete, ask the user.

Ask the user to name any enterprises they already want on the list. Add them as seeds.

**Startups and scale-ups.** For each company type and each city:

1. `search "<company type> company headquartered in <city>" --category company --num 10`
2. `search "<city> <company type> raises funding round" --since <one year ago> --num 6`

Then one `answer` per company type: "Which are the leading <company type> companies in <region>? Name the companies, their cities and their latest funding."

**Enterprises.** Company searches return startups, because enterprises rarely appear in funding news. For enterprise types, such as banks, insurers or law firms, search for signs of the need instead:

1. `search "<enterprise type> <city> hiring <the team that would use the product> engineer" --since <six months ago> --num 10`
2. `search "<enterprise type> <city> engineering blog OR case study <what the user's product does>" --since <one year ago> --num 10`

Keep an enterprise only if a source shows the need: a job ad, a post, a talk or a vendor case study.

Then pick the three strongest buyers found as seeds. Strongest means a close fit to "Who buys" and named funding, named customers or a sign of the need. Run Mirror mode on those seeds to fill the list.

## Rules for Mirror and Build

- Drop directories, listicles, media, consultancies and duplicates by domain.
- Drop the competitors in `company.md` and any company that sells the same product as the user. List what you dropped as a competitor in the review, so the user can check it.
- A company must have its headquarters or a real office in the region.
- Look for activity in the last 18 months: funding, a launch, open roles or a dated post. If the sources show none, keep the company, write "activity unconfirmed" and put it lower in the list.
- The city must come from the source. Write "unconfirmed" if it does not.
- Companies with named funding, named customers or a sign of the need go first.
- At most 30 new accounts per run.
- Mark any company already in `target-accounts.csv` as "on list".

## Domain check

For each account with no domain, run `search "<account>" --category company --num 3`. Take the domain only from a result whose title or URL contains the account name. If no result matches, write "unconfirmed".

## Review

Show the user the list as a table: Account | Domain | City | Tier | Why | On list | Source. Under it, list the companies dropped as competitors. Then ask the user to:

1. Remove accounts that are wrong or off limits.
2. Restore any dropped company that is not a competitor.
3. Confirm or change tiers.
4. Add owners, or leave them blank.

Write the approved list to `field/target-accounts.csv`. New accounts get status "new" unless the user gives one. Never remove or overwrite an existing row without the user's approval.

## Output

For Mirror and Build, also write `field/out/accounts-<region>-<date>.md`:

1. **Accounts found.** The review table.
2. **Clusters.** Table: City | Accounts | Main type | Read. Then two or three sentences on which city to start in and which event format fits each cluster.
3. **Where the list breaks.** Company types with no match in the region. Clusters in the region with no seed precedent. Mark inference as inference.
4. **Gaps.**
