# Events

Which rooms are most likely to reach the target accounts? Three kinds: conferences, events competitors run, and recurring meetups someone else already runs.

Public pages rarely show who attends. Sponsor lists are often images, and attendee lists are private. So this workflow ranks rooms by audience fit and by the target accounts named on speaker pages. Confirmed attendance comes from two places only: the organiser's list, and the team's own guest lists in the ledger.

Inputs: competitors and region from `company.md`, target accounts from `target-accounts.csv`, and the plan's 90 days as the window unless the user gives another. For meetups, use the cities with three or more target accounts, or the single city with the most.

## Research

1. **Competitors.** For each competitor: `search "<competitor> event OR sponsor OR meetup OR dinner <region>" --since <one year ago>`. Note the format, place and date. Past events stay in this table, because they show where competitors go.
2. **Conferences.** `search "<buyer type> conference <city or country> <year>"` and `answer "Which conferences and summits in <region> between <today> and <end of window> attract <who to meet>?"`. Drop conferences dated before today. For each conference, find its speaker page and `fetch <url>`. Mark every target account named in the page text. A sponsor page is worth a fetch too, but logos in images cannot be read.
3. **Meetups.** In each city: `search "<who to meet> meetup OR demo night OR community <city>" --since <one year ago>` and `answer "Which recurring meetups and communities in <city> bring together <who to meet>? How often do they meet and how many attend?"`. A recurring meetup meets more than once. Drop any with no event in 6 months.

## Output

`field/out/events-<region>-<date>.md`:

1. **Competitor history.** Table: Competitor | Event | Format | City | Date | Source. Say so when the research found no events for a competitor.
2. **Conferences.** Table: Event | City | Date | Audience | Fit | Target accounts on speaker page | Source. Fit is high, medium or low against "Who to meet" in `company.md`, with one reason.
3. **Meetups.** Table: Meetup | Run by | How often | Size | Last seen | Target accounts seen | Source. Say which are open to co-hosting and which sell sponsorship.
4. **The gap.** Formats, cities and audiences no competitor covers.
5. **Recommendation.** At most five events, meetups or own formats for the 90 days, each with one line on why and which target accounts it could reach.
6. **Ask the organisers.** For each recommended conference or meetup, one line to send the organiser asking for the sponsor list or the attendee companies. Draft only. Never send.
7. **Gaps.**
