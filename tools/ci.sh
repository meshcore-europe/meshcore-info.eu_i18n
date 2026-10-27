#!/usr/bin/env bash
# Checks for the translations repository, as its CI runs them. Generated
# from the site repository (tools/i18n-repo/); edit it there.
set -euo pipefail
cd "$(dirname "$0")/.."
echo "== interface text"
python tools/validate_i18n.py
echo "== pages"
python tools/validate_pages.py
echo "== glossaries"
python tools/sync_glossary.py --validate
echo "== coverage"
python tools/gaps.py
echo "== copy rules (tools/grade_copy.py) on what this change translates"
base="origin/${GITHUB_BASE_REF:-main}"
if git rev-parse --verify --quiet "${base}^{commit}" >/dev/null; then
  python tools/grade_copy.py --since "$base" --check
else
  echo "no ${base} to compare with: skipped"
fi
