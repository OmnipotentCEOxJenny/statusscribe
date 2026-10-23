# Changelog

## 1.0.2 (2026-10-23)
- Remove internal notes from the README, translations, rule file (renamed to `rules/scope.mdc` where applicable) and skills. Local tests re-run and passed. Not tested in-app. Not submitted to the marketplace.

## 1.0.1 (2026-10-23)
- Translations: each language section in TRANSLATIONS.md now starts with a one-line notice in that language saying it is a machine translation, not reviewed by a native speaker, and that the English version is authoritative. README Languages section notes this. No behavior changes.
- Local tests re-run and passed. Not tested in-app. Not submitted to the marketplace.

## 1.0.0 (2026-10-22)
- First version: skills `statusscribe-write` and `statusscribe-check`, rule `scope.mdc`, optional checker `scripts/statusscribe_check.py`, before-and-after example (real Course 4 memo), plain-language README.
- Tests: `tests/check_frontmatter.py` and `tests/test_checker.py`.
- 40 search keywords (single words lowercase, joined words PascalCase, no hyphens, StatusScribe-specific, per Rob's keyword rules) in the manifest plus `keywords.md`; 23 machine-translated summaries (not native-reviewed).
- Local tests only; not tested in-app. Not submitted to the marketplace.
