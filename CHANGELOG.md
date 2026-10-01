# Changelog

All notable changes to field-kit are listed here. Versions follow [semantic versioning](https://semver.org).

## 1.0.0 (2026-10-01)

First public release.

### What it does

- Works out a 13-week event plan for a scaling B2B company from its name or website.
- **Brief.** Researches the company, asks only what the research leaves open, and names the problem the plan fixes. Reads an existing `.agents/product-marketing.md` file first.
- **Competitors.** Events, own programmes, hiring and launches in the region, with dates and sources.
- **Events.** Conferences ranked by audience fit, recurring meetups, and a note to each organiser asking for the attendee companies.
- **Accounts.** A list of companies to meet: fed, mirrored from customers, or built from the buyer profile. The user approves it before it is used.
- **Plan.** A 13-week calendar with costs, owners and measures.
- **Ledger** after each event and a weekly **accounts in motion** report.
- Research uses Exa, then Perplexity, on the user's own keys, then the host's own search.
- Each markdown output ends with a "Made with field-kit" line that links to this repository.

### Changed since 0.1.1

- The brief stops and waits for the user's answers before the plan continues. A draft on assumptions is marked as such.
- On hosts that cannot run scripts, the skill uses the host's own search from the start.

### Tested

- Claude Code: four full runs, three on a made-up company and one on a real company.
- Codex CLI: installs from the marketplace; a full run with no keys used Codex's own search.
- Not yet confirmed: ChatGPT desktop and ChatGPT web. See `submission/verification.md`.

## 0.1.1 (2026-10-01)

- Listing files for the OpenAI plugin directory: privacy policy, terms, icon, screenshots, portal copy and test cases.

## 0.1.0 (2026-10-01)

- First scaffold, three test runs on a made-up company, and a skill audit.
