# Submission test cases

These are test instructions, not claims that every case passed.
See [verification.md](verification.md) for recorded results.
Use an empty test folder for each case. Keep all generated files in `field/`.
Use fictional data for guest lists. Never commit test output.

## 1. Plan

**Prompt:** Build us an event plan for Attio.

**Setup:** Install field-kit. Run once with a valid Exa key and once without either search key or a local `.env`.

**Follow-up input:** This is a test brief, not Attio's actual strategy. Focus on London, Cambridge and Manchester.
Use a £20,000 cash ceiling, one marketer and two sales staff. Target growing B2B software companies.
Meet founders, heads of sales and revenue operations leads. Propose meeting and opportunity targets.
Contract value and past results are unknown. No private customers or roadmap claims may be named.

**Expected behaviour:** Load the skill and research the company. Write `field/brief.md` and ask the unanswered brief questions.
After answers, run competitors, accounts and events. Show the proposed account list for review.
Approve the reviewed list as test data before continuing. Do not write unapproved accounts to the target file.

**Expected output:** A brief, supporting research in `field/out/`, and a 13-week plan beginning next Monday.
The plan has no more than 600 words outside tables. Costs have sources or estimate labels.
No monetary pipeline target appears without a contract value. Markdown files end with Gaps.

**Search checks:** With Exa, inspect script output for `provider: exa`.
Without keys, expect exit code 2, one fallback message, then host search for the remaining run.

## 2. Competitors

**Prompt:** What are HubSpot, Pipedrive and folk doing at events in the UK?

**Setup:** Supply a test brief for Attio with a UK region and those three competitors.

**Expected behaviour:** Read the brief. Search the last 12 months for events and owned programmes.
Check hiring, partnerships and launches. Count roles rather than people. Mark missing evidence and inferences.

**Expected output:** `field/out/competitors-<subject>-<date>.md` with overview, event history, signals and implications.
Every factual claim has a source URL. Historical events remain visible. A lack of results is not proof of inactivity.

## 3. Events

**Prompt:** Which conferences and recurring meetups fit this brief over the next 13 weeks?

**Setup:** Use the same test brief. Supply an approved test target list after reviewing the accounts.

**Expected behaviour:** Search cities separately. Check event dates and current speaker pages.
Distinguish speakers, sponsors and confirmed attendees. Flag missing pages and old speaker lists.
Keep undated meetups last as date unconfirmed. Exclude events outside the requested window.

**Expected output:** `field/out/events-<subject>-<date>.md` with conferences, meetups and at most ten shortlist entries.
Include audience-fit reasons and source URLs. Do not send organiser questions or make bookings.

## 4. Accounts

**Prompt:** Build a list of companies we should meet from this brief. Ask me before saving the approved list.

**Setup:** Use the same test brief, with no existing target file. Say there are no required enterprise seeds.

**Expected behaviour:** Use Build mode, then Mirror on suitable seeds. Aim for 20 to 30 accounts.
Drop competitors, duplicates, consultancies and directories. Check domains and regional presence against sources.
Flag unknown city, activity or headcount. Show the review table before writing approved targets.

**Review input:** Remove one named proposed account. Confirm the remaining tiers and leave owners blank.

**Expected output:** A sourced account report and `field/target-accounts.csv` containing only the approved rows.
The CSV columns are `account,domain,owner,status,tier,notes`. New rows have status `new`.

## 5. Ledger

**Prompt:** Log our test dinner on 1 October 2026 in London. It cost £600 and we invited ten people.
Three people registered and two attended. Guest A and Guest B attended from Test Company A.
Guest C registered from Test Company B but did not attend. Leave sales outcomes blank.

**Setup:** Create a test brief and approve Test Company A and Test Company B as fictional target accounts.
Use `test-a.example` and `test-b.example` as their domains. All guests belong to targets, so no search is needed.
Keep this fixture and every result inside `field/`.

**Expected behaviour:** Match both attendees to the same target company. Count companies separately from people.
Do not look up people, send follow-up, or invent meetings, opportunities or pipeline.

**Expected output:** An attendee CSV in `field/out/` and one row in `field/ledger.csv`.
Record ten invited, three registered, two attended, two targets on the list and one target attended.
Report £300 per attendee and £600 per target company attended.
Leave owner, next step, meetings, opportunities and pipeline blank.
