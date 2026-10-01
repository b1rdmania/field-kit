# Ledger

Record who came, which target accounts were in the room, and what the event cost. One table holds every event, so the team can compare them.

Inputs:

- A guest list: a Luma, Eventbrite or event-app export, or a pasted list. Name, company and title are enough.
- `field/target-accounts.csv`.
- The event facts: name, date, format, city, cost, number invited.

Real guest lists contain personal data. Keep them in `field/`, which git ignores. Never commit them.

## Steps

1. Read the guest list. Normalise company names. Match each company to the target accounts by name and by domain.
2. For companies not on the target list, run one `search "<company>" --category company --num 1` to get what they do. Skip people lookups.
3. Write `field/out/attendees-<event>-<date>.csv` with these columns: name, company, title, target_account, registered, attended, what_company_does, source, owner, next_step. Leave owner and next_step blank. Sales fills them.
4. Append one row to `field/ledger.csv`. Create the file with this header if it does not exist:

   `event,date,format,city,cost,invited,registered,attended,targets_on_list,targets_attended,meetings,opportunities,pipeline`

   Fill the first ten columns. Leave meetings, opportunities and pipeline blank. They come from the sales system.

## Output

Tell the user: the target accounts that attended, cost per attendee, cost per target account attended, and how this event compares with earlier rows in `ledger.csv`.
