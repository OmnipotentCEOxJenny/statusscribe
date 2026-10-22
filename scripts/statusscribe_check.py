#!/usr/bin/env python3
"""StatusScribe status-update checker (standard library only).
Usage: python3 scripts/statusscribe_check.py FILE
Checks a status memo or progress update for: memo header (TO, FROM, DATE, SUBJECT), a full
written date, a purpose in the opening paragraph, sections for work done, next steps and
risks or limits, numbered next actions, clock times that name a time zone (a table whose header names the zone, e.g. "(ET)", counts), and vague words
("soon", "ASAP", "pretty well"). Rough heuristics only; it cannot check whether facts are true.
Exit 0 = all checks pass, 1 = something to fix, 2 = usage error."""
import re, sys

MONTHS = "January|February|March|April|May|June|July|August|September|October|November|December"
VAGUE = ["soon", "asap", "pretty well", "some stuff", "most stuff", "a few things", "going well", "at some point"]

def check(text):
    low = text.lower(); res = []
    def add(name, ok, detail=""): res.append((name, ok, detail))
    head = {f: bool(re.search(rf"^\s*{f}:\s*\S", text, re.M)) for f in ("TO", "FROM", "DATE", "SUBJECT")}
    add("memo-header", all(head.values()), "missing: " + ", ".join(k for k, v in head.items() if not v))
    add("full-date", bool(re.search(rf"\b({MONTHS}) \d{{1,2}}, \d{{4}}\b", text)), "write the date in full, e.g. October 22, 2026")
    body = re.sub(r"```.*?```", "", text, flags=re.S).strip()
    first = next((p for p in re.split(r"\n\s*\n", body) if p.strip() and not p.lstrip().startswith(("#", "|", "**", "-"))), "")
    add("purpose-first", bool(re.search(r"\b(this (memo|update|report)|purpose|gives|summari[sz]es)\b", first.lower())), "open with what the update is for")
    add("section-done", bool(re.search(r"\b(completed|done|finished|work completed)\b", low)), "say what was completed")
    add("section-next", bool(re.search(r"\bnext steps?\b", low)), "add a Next steps section")
    add("section-risks", bool(re.search(r"\b(risks?|limits?|blockers?|issues)\b", low)), "name risks, limits or blockers")
    add("numbered-actions", bool(re.search(r"^\s*1\.\s", text, re.M)), "number the actions the reader must take")
    zone_tables = bool(re.search(r"^\|.*\((?:ET|EST|EDT|UTC|PT|CT|MT|GMT)\)", text, re.M))
    scan = "\n".join(l for l in text.splitlines() if not (zone_tables and l.lstrip().startswith("|")))
    times = re.findall(r"\b\d{1,2}:\d{2}\s?(?:AM|PM)\b(?!\s?(?:ET|EST|EDT|UTC|PT|CT|MT|GMT))", scan)
    add("time-zones", not times, "add a time zone to: " + ", ".join(times[:5]))
    vague = [w for w in VAGUE if re.search(r"\b" + re.escape(w) + r"\b", low)]
    add("no-vague-words", not vague, "replace: " + ", ".join(vague))
    return res

def main(argv):
    if len(argv) < 2: print(__doc__); return 2
    res = check(open(argv[1], encoding="utf-8").read())
    for name, ok, detail in res:
        print(("ok   " if ok else "FIX  ") + name + ("" if ok else f": {detail}"))
    bad = sum(1 for r in res if not r[1])
    print("all checks pass (heuristic only; a human read is still needed)" if not bad else f"{bad} item(s) to fix (heuristic only)")
    return 1 if bad else 0

if __name__ == "__main__":
    sys.exit(main(sys.argv))
