#!/usr/bin/env bash
# For each problem folder: test every version, check every animation, then commit and push it on its own.
# Usage: tools/verify_and_push.sh 0088-merge-sorted-array 0027-remove-element ...
set -euo pipefail
cd "$(dirname "$0")/.."
BRANCH=$(git rev-parse --abbrev-ref HEAD)
for d in "$@"; do
  echo "=== $d"
  ok=0
  for attempt in 1 2 3; do  # retry: Maven Central sometimes answers 429 Too Many Requests
    if (cd "$d" && ./gradlew test -q --console=plain >/tmp/gradle-$d.log 2>&1); then ok=1; break; fi
    grep -q "429" /tmp/gradle-$d.log || break
    sleep 20
  done
  [ $ok = 1 ] || { grep -v JAVA_TOOL_OPTIONS /tmp/gradle-$d.log | tail -40; echo "TESTS FAILED: $d"; exit 1; }
  node tools/check_animations.js "$d"/v*/
  git add "$d"
  git diff --cached --quiet && { echo "unchanged $d"; continue; }
  title=$(head -1 "$d/README.md" | sed 's/^# //')
  versions=$(ls -d "$d"/v*/ | wc -l)
  if git cat-file -e "HEAD:gradle-java/$d/README.md" 2>/dev/null; then verb=Update; else verb=Add; fi
  msg="$verb $title"
  [ "$verb" = Update ] && [ -n "${UPDATE_NOTE:-}" ] && msg="$title: $UPDATE_NOTE"
  [ "$versions" -gt 1 ] && msg="$msg ($versions solution versions)"
  git commit -q -m "$msg"
  for wait in 2 4 8 16 0; do
    git push -q -u origin "$BRANCH" && break
    [ "$wait" = 0 ] && { echo "push failed"; exit 1; }
    sleep "$wait"
  done
  echo "pushed $d: $msg"
done
