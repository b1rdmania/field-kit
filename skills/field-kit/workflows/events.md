# Events

Where should the company show up? Conferences where the buyers go, and recurring meetups someone else already runs.

Public pages rarely show who attends. Sponsor lists are often images, and attendee lists are private. So this workflow ranks rooms by how well the audience fits the buyers, and by the companies named on speaker pages. Confirmed attendance comes from the organiser's list or the team's own guest lists in the ledger.

Inputs: buyers and region from the brief, the competitors output if it exists, and `target-accounts.csv` if it exists. The window runs from today to 13 weeks after next Monday unless the user gives another.

## Research

1. **Conferences.** `search "<buyer type> conference <city or country> <year>"` and `answer "Which conferences and summits in <region> between <today> and <end of window> attract <who to meet>?"`. Drop conferences dated before today. For each conference, find its speaker page and `fetch <url>`. Note the companies on it, and mark target accounts with the match rule in SKILL.md. A sponsor page is worth a fetch too, but logos in images cannot be read. If there is no speaker page yet, or it shows last year's speakers, say so in the table.
2. **Meetups.** In the two or three cities with the most buyers: `search "<who to meet> meetup OR demo night OR community <city>" --since <one year ago>` and `answer "Which recurring meetups and communities in <city> bring together <who to meet>? How often do they meet and how many attend?"`. A recurring meetup meets more than once. For the last date seen, look for dated listings (Meetup, Luma, Eventbrite). If the page shows no date, run `search "<meetup name>" --since <six months ago>` and take the newest dated result. Drop a meetup only when the newest date is older than 6 months. If no date is found, keep it as "date unconfirmed" and put it last.

## Output

`field/out/events-<region>-<date>.md`:

1. **Conferences.** Table: Event | City | Date | Audience | Fit | Competitors present | Companies on speaker page | Source. Fit is high, medium or low against the buyers in the brief, with one reason.
2. **Meetups.** Table: Meetup | Run by | How often | Size | Last seen | Source. Say which are open to co-hosting and which sell sponsorship. If the source does not say, write "terms not published".
3. **Shortlist.** At most ten events, meetups or formats the team could run itself, each with one line on why.
4. **Ask the organisers.** For each shortlisted conference or meetup, one line to send the organiser asking for the attendee companies or the sponsor list.
