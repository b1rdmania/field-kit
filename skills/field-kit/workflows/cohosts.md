# Co-hosts

Who already runs the room for an audience in a city? A co-host brings the audience. The team brings the content and the budget.

Inputs: a city and an audience. Take the audience from "Who to meet" in `company.md` if the user does not give one.

## Research

1. `search "<audience> meetup <city>" --since <one year ago>`
2. `search "<audience> demo night OR hackathon OR community <city>"`
3. `answer "Which recurring meetups, demo nights and communities in <city> bring together <audience>? How often do they meet and how many attend?"`
4. For each community found, search for past sponsors and speakers. Mark target accounts that appear.

## Rules

- A recurring room meets more than once. List one-off events separately.
- Organisations only, unless a public page names the organiser in that role.
- Give the last date seen. A community with no event in 6 months goes to the bottom.

## Output

`field/out/cohosts-<city>-<date>.md`:

1. **Recurring rooms.** Table: Community | Run by | How often | Size | Audience | Last seen | Target accounts seen | Source.
2. **One-offs.** The same table, shorter.
3. **Best fit.** The two or three rooms that hold the audience the team wants. Say which slots are paid sponsorship and which are co-host.
4. **Gaps.**
