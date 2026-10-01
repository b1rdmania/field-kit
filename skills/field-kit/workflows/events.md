# Events

Which rooms reach the target accounts? Three kinds: conferences where they already go, events competitors run, and recurring meetups someone else already runs.

Inputs: competitors and region from `company.md`, target accounts from `target-accounts.csv`, and the plan's 90 days as the window unless the user gives another. Drop every event with a date before today. For meetups, use the one or two cities with the most target accounts unless the user names a city.

## Research

1. **Competitors.** For each competitor: `search "<competitor> event OR sponsor OR meetup OR dinner <region>" --since <one year ago>`. Note the format, place and date.
2. **Conferences.** `search "<buyer type> conference <region> <year>"` and `answer "Which conferences and summits in <region> between <today> and <end of window> attract <who to meet>?"`. For each major event, find its sponsor or speaker page, then `fetch <url>`. Mark every target account named in the page text. If no page lists them, write "not published".
3. **Meetups.** In each city: `search "<who to meet> meetup OR demo night OR community <city>" --since <one year ago>` and `answer "Which recurring meetups and communities in <city> bring together <who to meet>? How often do they meet and how many attend?"`. A recurring meetup meets more than once. Drop any with no event in 6 months.

## Output

`field/out/events-<region>-<date>.md`:

1. **Competitors.** Table: Competitor | Event | Format | City | Date | Source. Say so when the research found no events for a competitor.
2. **Conferences.** Table: Event | City | Date | Audience | Competitors present | Target accounts present | Source.
3. **Meetups.** Table: Meetup | Run by | How often | Size | Last seen | Target accounts seen | Source. Say which are open to co-hosting and which sell sponsorship.
4. **The gap.** Formats, cities and audiences no competitor covers. Rooms with many target accounts and no competitor present go first.
5. **Recommendation.** At most five events, meetups or own formats for the next 90 days, each with one line on why and which target accounts it reaches.
6. **Gaps.**
