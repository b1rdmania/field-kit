# Brief

Write `field/brief.md` from the company's name or website. Research first, then ask only what the research could not answer.

## Research

1. `fetch <company website>`. Read the homepage, then the product, pricing, customers and careers pages if they exist. Take customer names only from a customers or case-study page, or a logo wall labelled as customers. Names inside product screenshots or demos are sample data, not customers.
2. `search "<company> competitors OR alternatives" --num 10` and `search "<company> vs" --num 10`.
3. `search "<company> funding OR raises" --num 5` for stage and size.
4. `search "<company> event OR conference OR sponsor OR meetup" --since <one year ago> --num 10` for past events.

## Draft

Copy `templates/brief.md` to `field/brief.md` and fill each section from the research. Mark every guess "(guess)". If `.agents/product-marketing.md` or similar exists, take what it says over your research.

## Ask

Show the draft. Then ask these questions in one message. Skip any that the research or a context file already answers:

1. **Buyers.** Which company types buy, and which job titles choose the product?
2. **Region.** Where should the events happen?
3. **Budget and time.** What can you spend on events in the next 13 weeks, and who will run them?
4. **Past events.** Which events have you done, and what came of them?
5. **What a win is.** Meetings, opportunities, pipeline? What is a first-year contract worth?
6. **Off limits.** Anything that must not be claimed or named?

Update the brief with the answers. Remove "(guess)" from anything the user confirmed.

## Diagnose

End the brief with **The problem**: one or two of the problems in SKILL.md's table, with the evidence from the research and answers. Example: "No list of who to meet. You named buyer types but no companies." Then name the workflow that fixes it first.
