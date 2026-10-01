# Verification report

Checked 1 October 2026. Baseline: `9b5df05`. Codex CLI: `0.159.3`.
The tests used the configured Codex model, GPT-6-Astra, with medium reasoning.

No directory upload, submission, publication or Git push was made.
The package files are prepared locally. The checks below must be resolved before calling the release fully verified.

## 1. Codex CLI install

Status: passed against the live repository at `9b5df05`, version `0.1.0`.

`codex plugin marketplace add b1rdmania/field-kit` found the existing marketplace at the expected GitHub URL.
The `/plugins` browser found field-kit and installed it. It listed `field-kit:field-kit` and reported no authentication requirement.
No manifest error appeared. The installed skill matched the working copy.

The terminal initially used `TERM=dumb`, which the interactive CLI refused.
Setting `TERM=xterm-256color` allowed the plugin browser to open. No package change was needed.

## 2. Codex runs

### Exa

Status: blocked, not run.

`EXA_API_KEY` was absent. Neither the working folder nor the home folder contained a `.env` file.
A request for an existing key file path had no answer during this task.
Perplexity was available in the parent environment, but it was not used as a substitute for the requested Exa test.

Next: set a valid Exa key outside chat. Use an empty test folder and the prompt below.
Confirm successful script responses name Exa as the provider. Complete the brief and account review steps.
Check `field/brief.md`, `field/out/` and all 13 calendar weeks.

### No keys

Status: full draft produced; search fallback passed; brief question step failed.

Prompt: `Build us an event plan for Attio.`

The test started in an empty folder with both provider keys removed from the environment.
A separate shell check confirmed that neither key returned through shell startup.
The folder contained no `.env`.

Observed results:

- Codex found and read the installed field-kit skill without an explicit skill mention.
- It called the installed `scripts/search.py` to fetch Attio's site.
- The script reported that fetch needs Exa. A separate no-key search returned exit code 2.
- Codex gave the prescribed fallback message once, then made 26 host web calls.
- It wrote `field/brief.md` and plan, competitors, events and accounts reports in `field/out/`.
- The calendar had weeks 1 through 13, starting Monday 5 October 2026.
- The plan had 355 words outside tables. It labelled costs as estimates and unknown inputs as guesses.
- It proposed 20 accounts. It did not write an approved `field/target-accounts.csv` without review.
- All six Markdown files had a Gaps section. The run ended successfully.

The model researched and drafted the plan before asking the brief's required questions.
It asked for account review at the end, but never asked the full brief questions.
The brief also claimed those questions had been asked. That claim was false.
The files are a provisional draft, not an approved event plan.

Suggested fix: require the brief workflow to pause after its questions, unless the user explicitly asks for an assumed draft.
Repeat this test after any instruction change. This task records the failure and leaves workflow behaviour unchanged.

The host reported an unrelated `mobai` startup failure and a temporary plugin-directory 503.
Neither stopped the installed skill or the no-key run.

Local evidence remains under the ignored `field/verification/` folder.
It includes the JSONL run log and the test folder `no-keys/`.
No research output, proposed account list or raw log belongs in the submission ZIP.

## 3. ChatGPT desktop

Status: blocked by the computer-use tool.

The app inventory showed ChatGPT running. Selecting it returned:

> Computer Use is not allowed to use the app 'com.openai.codex' for safety reasons.

No workaround was attempted. CLI installation does not prove desktop skill loading or script execution.

Next: open the desktop plugin directory manually and select the field-kit marketplace.
Confirm installation, skill loading and a `scripts/search.py` call in a fresh Work or Codex task.

## 4. ChatGPT web

Status: upload entry point confirmed; skill installation and fallback unconfirmed.

In a signed-in Firefox session, ChatGPT showed Plugins, Skills and Add skill.
The Add skill menu offered Upload from your computer.
Two attempts to continue were interrupted by browser activity. The test tab then closed.
A separate Safari check reached a signed-out ChatGPT page, which required login for uploads.
No skill upload or web research run completed.

Next: upload `skills/field-kit` through the Skills page using the file format requested by the picker.
Ask for an Attio event plan. Confirm that ChatGPT uses its own search when the script cannot run.
Do not mistake a personal skill upload for a public directory submission.

The skill currently describes fallback after script exit code 2.
It does not explicitly describe a host with no script runner. Check that case before claiming web support is verified.

## 5. Directory submission preparation

Status: local files prepared; no submission made.

Added privacy and terms pages, skill display metadata, a square SVG icon and two labelled fictional screenshots.
Added portal copy and five test cases: plan, competitors, events, accounts and ledger.
The test cases are reviewer instructions. They are not five completed test runs.

Updated both package versions to `0.1.1`. Added the listing URLs, icon paths, screenshots and starter prompts.
Shortened the listing subtitle to fit the current 30-character submission limit.
The workflows and search script are unchanged.

The finished ZIP installed through Codex from a clean temporary marketplace as version `0.1.1`.
An earlier local test placed its cache inside the source folder and hit a file-name-too-long error.
Moving the test home outside the package source fixed it. The failed test cache was removed.

The public privacy and terms URLs point to files in `main`. Publish the commits before relying on those URLs.
Confirm the verified publisher name and recheck the remaining tests before submitting.

Field names and image rules were checked against the official documentation:

- [Package your plugin](https://developers.openai.com/plugins/build/plugins)
- [Upload and submit your plugin](https://developers.openai.com/plugins/deploy/submission)
