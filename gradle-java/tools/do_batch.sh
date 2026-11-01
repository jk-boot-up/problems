#!/usr/bin/env bash
# Generate everything, check one batch's animations, then test + commit + push each of its projects separately.
set -euo pipefail
cd "$(dirname "$0")/.."
python3 tools/generate.py
dirs=$(python3 tools/generate.py --dirs "$1")
# projects pushed earlier that changed because the shared engine changed
changed=$(git status --porcelain -- . | sed -E 's#^.. (gradle-java/)?##' | grep -oE '^[0-9]{4}-[a-z0-9-]+' | sort -u || true)
for c in $changed; do case " $dirs " in *" $c "*) ;; *) dirs="$c $dirs";; esac; done
tools/verify_and_push.sh $dirs
git add README.md settings.gradle.kts tools
if ! git diff --cached --quiet; then
  git commit -q -m "Update problem index and generator"
  git push -q origin HEAD
fi
echo "BATCH DONE $1"
