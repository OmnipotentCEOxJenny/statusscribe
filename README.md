# StatusScribe

StatusScribe helps your AI assistant write status updates people actually read. You give it your notes. It turns them into a short memo or progress report: a subject line that says the headline, what got done, what is waiting, what could go wrong, and a numbered list of what the reader needs to do. Then it checks the update for missing parts, vague words and times without a time zone. Why would you want this? Busy readers skim. A clear update saves meetings, prevents surprises and gets decisions made faster. It's free.

![StatusScribe logo](assets/logo.png)

## Project status: done, pending, uncertain
**Done**
- 2026-10-22: v1.0.0 built and pushed to GitHub. Local tests: manifest valid JSON and valid against Cursor's plugin schema, skill and rule front matter valid (`tests/check_frontmatter.py`), and `tests/test_checker.py` confirms the checker flags the vague "before" update and passes the real "after" memo.

**Pending**
- Not tested inside Cursor or Grok yet (no in-app test has been done).
- Not submitted to the marketplace.
- Translated summaries are machine-made and not reviewed by native speakers.

## Quick start
1. Install (see Installation).
2. Ask: "Turn these notes into a status memo for my manager."
3. Then ask: "Check this update with StatusScribe."

## Installation
Install from this repository: https://github.com/OmnipotentCEOxJenny/statusscribe (Cursor plugin format: `.cursor-plugin/plugin.json`, `skills/`, `rules/`). Free. No API keys, no accounts, no paid services. The optional checker needs only Python 3 (standard library).

## Testing
1. `python3 tests/check_frontmatter.py` (needs PyYAML).
2. `python3 tests/test_checker.py`. Expected: PASS.
3. Compare with `examples/`.

## Search keywords
StatusScribe, JennyEcho, OmnipotentCeo, status, update, updates, memo, memos, progress, report, reporting, weekly, daily, standup, recap, summary, briefing, accomplishments, blockers, NextSteps, actions, decisions, handoff, team, manager, boss, clients, email, subject, header, professional, workplace, correspondence, informing, TimeZone, dated, candor, accountability, digest, headline. The full list with plain-word meanings is in [keywords.md](keywords.md).

## Credits
- Inventor and publisher: Rob Domaine / Omnipotent Media LLC
- Builder: Jenny Echo
- Guidance drawn from free open textbooks Jenny Echo studied:
  - Sam Schechter and Nathan Hall, *Professional Writing in the Digital Age*, 2026, CC BY-NC-SA 4.0 (Course 4: memo format, seven Cs, delivering bad news).
  - Adrienne Watt, *Project Management*, 2nd edition, BCcampus, CC BY 4.0 (Course 5: communication planning).
  - Suzan Last, *Technical Writing Essentials*, University of Victoria, 2019, CC BY 4.0 (Course 3: progress reports).
- Summarized in our own words; StatusScribe is independent and not endorsed by the authors.

## Components
- `skills/statusscribe-write`: write the update from the user's notes.
- `skills/statusscribe-check`: check an update before sending.
- `scripts/statusscribe_check.py`: optional automatic first pass (standard library only).
- `examples/`: a vague update and a real memo.
- `tests/`: front-matter check and functional checker test.
- `rules/scope.mdc`: the scope.
- `keywords.md`: the search keyword list.

## Languages
The AI answers in the user's language and keeps commands, file names and code unchanged. Summaries in 23 languages are in [TRANSLATIONS.md](TRANSLATIONS.md). They are machine translations, not yet reviewed by native speakers; the English text is authoritative. Each language section in TRANSLATIONS.md also starts with a one-line machine-translation notice in that language.

## License
MIT. See `LICENSE`.

## Honest assessment: what this plugin cannot do
- It has not been tested inside Cursor or Grok yet; only local tests on one computer have been run.
- It does not send anything; you send the update yourself.
- It cannot know whether your progress figures are true; it only writes and checks what you give it.
- The automatic checker is a rough English-only heuristic and can miss problems or flag fine text.
- It is not legal or HR advice.
- Marketplace: not submitted; it is not an approved listing.
- Translations are machine-made and not reviewed by native speakers.
- Rules and compliance: it follows all local, county, state and federal laws and every platform's rules, uses no paid services, never bypasses logins or security settings, and never claims a feature it does not have.
