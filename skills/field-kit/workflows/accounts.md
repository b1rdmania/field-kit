# Accounts

Build or check the list of companies to meet: the target accounts. The plan, the events workflow, the ledger and the weekly report all mark these companies in their results.

| The user has | Mode |
| --- | --- |
| A target list, pasted or as a CSV | **Feed** |
| Customers or example accounts, and wants more like them | **Mirror** |
| Nothing yet | **Build** |

Pick the mode from what the user has. Ask only if they gave both a list and examples. Every mode ends with the domain check and the review.

## Feed

1. Map the list's columns to `account,domain,owner,status,tier,notes`. Remove duplicates by domain, then by name.
2. Propose a tier where none is given. Tier 1 fits "Who buys" in the brief best. Give one reason per tier 1 account.
3. Keep any owner or status the user gave.

If the list has fewer than 20 accounts, offer Mirror with the list as seeds.

## Mirror

Seeds come from "Customers we can name" in the brief, the current target list, or examples the user names. A seed buys, or would buy, what the user sells. It is never a vendor of a similar product. Seeds stay on the list.

Run the lookalike search for each seed. Use the need search instead when the seed is an enterprise.

## Build

Aim for 20 to 30 approved accounts.

1. Turn "Who buys" into two or three concrete types. A concrete type names a product and a buyer: "contract review software for law firms", not "AI-native software company". Ask the user if you cannot.
2. Ask the user to name enterprises they already want. Add them as seeds.
3. Run the lookalike search for each startup or scale-up type, and the need search for each enterprise type.
4. Pick the three strongest buyers as seeds: closest to "Who buys", with named funding, named customers or a sign of the need. Run Mirror on them.

## Searches

Run each search once per city in the region.

**Lookalike search** for a description D (what a seed does, or a company type):

1. `search "<D> company headquartered in <city>" --category company --num 10`
2. `search "<city> <D> raises funding round" --since <one year ago> --num 6`
3. Once per D, not per city: `answer "Which are the leading <D> companies in <region>? Name them, their cities and their latest funding."`

**Need search** for an enterprise type E. Enterprises rarely appear in funding news, so search for signs that they need the product:

1. `search "<E> <city> hiring <team that would use the product> engineer" --since <six months ago> --num 10`
2. `search "<E> <city> engineering blog OR case study <what the product does>" --since <one year ago> --num 10`

Keep an enterprise only if a source shows the need: a job ad, a post, a talk or a vendor case study.

## What to keep

- Drop directories, media, consultancies and duplicates.
- Drop competitors from the brief and anyone selling the same product.
- Keep only companies with a headquarters or real office in the region. The city must come from a source, or write "unconfirmed".
- Look for activity in the last 18 months. If none is found, keep the company as "activity unconfirmed" and rank it lower.
- Rank named funding, named customers and signs of the need first. At most 30 new accounts per run.

## Domain check

For each account with no domain, use the company's own site if the research found it. Otherwise run `search "<account> <city> <what it does>" --category company --num 3`. Take the domain only when the result is the company's own site and matches its city and business. A name match alone is not enough. If two results fit, or none does, write "unconfirmed".

## Review

Show a table: Account | Domain | City | Tier | Why | Source. Mark accounts already on the list. Under the table, list the competitors you dropped. Ask the user to remove wrong accounts, restore wrongly dropped ones, confirm tiers and add owners.

Write only the approved list to `field/target-accounts.csv`. New accounts get status "new". Never change an existing row without approval.

## Output

For Mirror and Build, also write `field/out/accounts-<region>-<date>.md`:

1. **Accounts.** The review table.
2. **Clusters.** City | Accounts | Main type, then two or three sentences on which city to start in and which format fits each.
3. **Where the list breaks.** Types with no match, and clusters with no seed. Mark inference as inference.
