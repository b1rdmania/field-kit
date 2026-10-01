# OpenAI plugin submission copy

Package type: skills only. The plugin has no MCP server.
This file prepares the listing. It does not authorize a submission.

## Listing

- Name: field-kit
- Developer: b1rdmania
- Category: Productivity
- Short description: Plan events that reach buyers
- Website: https://github.com/b1rdmania/field-kit
- Support: https://github.com/b1rdmania/field-kit/issues
- Privacy: https://github.com/b1rdmania/field-kit/blob/main/PRIVACY.md
- Terms: https://github.com/b1rdmania/field-kit/blob/main/TERMS.md
- Icon and logo: `assets/icon.svg`
- Screenshots: `assets/screenshot-plan.jpg` and `assets/screenshot-ledger.jpg`

## Long description

Give field-kit your company name or website. It researches your buyers, competitors and events, then drafts a brief.
Answer the gaps and review the companies you want to meet.

Build a 13-week event calendar with costs and owners. Compare conferences, recurring meetups and small events you run yourself.
After each event, log attendance and costs against your target companies. Use the weekly report to choose follow-up work.

Research includes source links and marks gaps. Costs without quotes are estimates.
Public speaker lists do not prove attendance. You review account matches and supply sales outcomes.

On hosts that can run Python and curl, field-kit searches Exa or Perplexity using your own API key.
If the script cannot run or no provider works, use the host's web search.
Provider charges and host limits may apply. field-kit does not send messages, book events or connect to your CRM.

## Starter prompts

1. Build us an event plan for Attio.
2. What are our competitors doing at events?
3. Log our latest event against our target accounts.

## Data and permissions

The package contains one skill, workflow instructions, templates and a Python search script.
It reads the company context and files the user supplies. It writes work to `field/` in the working folder.
The script sends search queries or page URLs to Exa or Perplexity with the user's key.
Fallback research uses the host's search tools. The publisher runs no server and receives no plugin telemetry.
The host and providers apply their own privacy policies and account settings.

## Release notes

Add privacy and terms pages, directory images, skill display metadata and five workflow test cases.
Record the Codex install and no-key run, plus the remaining verification gaps. Skill behaviour is unchanged.

## Before submission

1. Resolve the outstanding checks in [verification.md](verification.md).
2. Publish these files to the public repository, then check all listing URLs.
3. Confirm that the verified developer identity displays the intended public name, b1rdmania.
4. Review the fictional screenshot labels and the five [test cases](test-cases.md).
5. Build the ZIP with `python3 submission/package.py`.
6. Use `field/submission/field-kit-listing-assets-0.1.1.zip` for listing images, copy and policies.
7. Use `field/submission/field-kit-0.1.1.zip` for the installable plugin.
8. Review the archive contents before uploading it yourself.

No upload to OpenAI or directory submission has been made.

## References

Field names follow [Package your plugin](https://developers.openai.com/plugins/build/plugins).
Image rules follow [Upload and submit your plugin](https://developers.openai.com/plugins/deploy/submission).
Checked 1 October 2026. Skills-only plugins do not use MCP review test-case metadata.
