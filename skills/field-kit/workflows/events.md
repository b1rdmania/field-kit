# Events

Where do competitors run events in the region, which events do the target accounts attend, and where is the gap?

Inputs: competitors and region from `company.md`, target accounts from `target-accounts.csv`, and the next 6 to 12 months as the window.

## Research

1. For each competitor: `search "<competitor> event OR sponsor OR meetup OR dinner <region>" --since <one year ago>`. Note the format (conference sponsor, own event, dinner, meetup, hackathon), place and date.
2. The region's calendar: `search "<buyer type> conference <region> <year>"` and `answer "Which conferences and summits in <region> in the next 12 months attract <who to meet>?"`.
3. For each major event found, search for its speaker or sponsor list. Mark every target account that appears.

## Output

`field/out/events-<region>-<date>.md`:

1. **Competitors.** Table: Competitor | Event | Format | City | Date | Source. Say so when the research found no events for a competitor.
2. **Calendar.** Table: Event | City | Date | Audience | Competitors present | Target accounts present | Source.
3. **The gap.** Formats, cities and audiences no competitor covers. Events with many target accounts and no competitor present go first.
4. **Recommendation.** At most five events or formats for the next 90 days, each with one line on why and which target accounts it reaches.
5. **Gaps.**
