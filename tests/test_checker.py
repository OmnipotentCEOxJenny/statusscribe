#!/usr/bin/env python3
"""Functional test: the checker flags the vague 'before' update and passes the real 'after' memo."""
import pathlib, sys
root = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(root / "scripts"))
from statusscribe_check import check
bad = {n for n, ok, _ in check((root / "examples/before.md").read_text(encoding="utf-8")) if not ok}
good = [n for n, ok, _ in check((root / "examples/after.md").read_text(encoding="utf-8")) if not ok]
need = {"memo-header", "full-date", "section-next", "numbered-actions", "no-vague-words"}
print("before.md failures:", sorted(bad)); print("after.md failures:", good)
ok = need <= bad and not good
print("PASS" if ok else "FAIL"); sys.exit(0 if ok else 1)
