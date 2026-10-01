# Competitors

What are the competitors doing to reach buyers? Events first, then the other signs of where they are pushing.

Inputs: competitors and region from the brief. Use the last 12 months. For each competitor, search the whole region once and the main city once. Do not split by every city.

## Research

For each competitor:

1. **Events.** `search "<competitor> event OR sponsor OR meetup OR dinner OR booth <region or main city>" --since <one year ago>`. Note the format, place and date.
2. **Own programmes.** `search "<competitor> community OR user group OR conference OR summit OR roadshow" --since <one year ago>`. Their own event or community, if they run one.
3. **Hiring.** `search "<competitor> hiring events manager OR field marketing OR community manager OR account executive <region>" --since <six months ago>`. New roles show where they plan to grow. Use job pages and company career pages. Count roles, not people. Ignore personal profiles.
4. **Partnerships and launches.** `search "<competitor> partnership OR launch <region>" --since <six months ago>`.

## Output

`field/out/competitors-<region>-<date>.md`:

1. **At a glance.** Table: Competitor | Events in 12 months | Own programme | Hiring in region | Read. The read is one line: where they are pushing.
2. **Event history.** Table: Competitor | Event | Format | City | Date | Source. Past events stay in, because they show where competitors go.
3. **Signals.** Table: Competitor | Signal | Date | Source. Hiring, partnerships and launches.
4. **What it means.** Three to five lines: rooms the competitors own, rooms nobody covers, and formats nobody runs.
