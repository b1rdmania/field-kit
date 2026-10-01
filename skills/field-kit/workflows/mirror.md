# Mirror

Find the companies in a region that look like the team's customers or target accounts.

Two modes:

- **Mirror.** Seeds are the customers in `field/customers.csv` or the target accounts in `field/target-accounts.csv`. The output is new companies in the region that match the seeds.
- **Expand.** The user has a target list and wants it longer. Use the target accounts as seeds and keep only companies not already on the list.

Ask which seeds to use if the user does not say. Ask for the region if `company.md` does not give one.

## Research

For each seed:

1. `search "<what the seed does>, company headquartered in <region>" --category company --num 10`
2. `search "<region> startup building <what the seed does> raises funding round" --since <one year ago> --num 6`
3. Find the seed's homepage, then `similar <homepage> --num 10`.

Then one `answer` per seed: "Which <region> companies are the best-known equivalents of <seed> (<what it does>)? Name the companies, their cities and their latest funding."

Drop directories, listicles, media, consultancies and the seeds themselves. Drop duplicates by domain.

## Rules

- A company must have its headquarters or a real office in the region.
- A company must show activity in the last 18 months in the source: funding, a launch, open roles or a dated post.
- The city must come from the source. Write "unconfirmed" if it does not.
- Companies with named funding, named customers or a known product go first.
- At most 30 rows.
- Mark any company already in `target-accounts.csv` as "on list".

## Output

`field/out/mirror-<region>-<date>.md`:

1. **The mirror.** Table: Company | City | Mirrors | What they build | Activity | On list | Source.
2. **Clusters.** Table: City | Companies | Main type | Read. Then two or three sentences on which city to start in and which event format fits each cluster.
3. **Where the mirror breaks.** Seed types with no match in the region. Clusters in the region with no seed precedent. Mark inference as inference.
4. **Gaps.**

Offer to append the new companies to `field/target-accounts.csv` with status "mirror" and no owner. Write to the file only if the user says yes.
