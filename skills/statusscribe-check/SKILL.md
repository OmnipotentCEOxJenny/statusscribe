---
name: statusscribe-check
description: Check a status update or memo for missing parts, vague words, unchecked facts and times without a time zone. Use when a user asks to review or improve a status update, memo or progress report.
---

Follow `rules/scope.mdc`. Answer in the user's language.

1. Check the header (TO, FROM, DATE, SUBJECT), the full date and that every clock time names a time zone.
2. Check the opening states the purpose and overall state.
3. Check for Completed, Next steps and Risks or limits sections, and numbered actions for the reader.
4. Check facts: every version, count, date and time matches its source; anything unchecked is marked UNVERIFIED.
5. Check tone: clear first, concise, courteous; no vague words; no confidential details.
6. If Python is available, run `python3 scripts/statusscribe_check.py FILE` for an automatic first pass. It is a rough heuristic and cannot judge whether facts are true.
7. Report each item as ok or FIX with a suggested rewrite.
