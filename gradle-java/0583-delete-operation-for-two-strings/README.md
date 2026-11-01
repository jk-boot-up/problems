# 583. Delete Operation for Two Strings

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Dynamic Programming &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/delete-operation-for-two-strings/)

## Problem

Return the minimum number of single-character deletions (from either string) needed to make `word1` and `word2` equal.

**Example**
```
"sea", "eat"       → 2   (delete 's' and 't')
"leetcode", "etco" → 4
```

**Constraints**
* `1 <= length <= 500`, lower-case letters

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-longest-common-subsequence](v1-longest-common-subsequence/README.md) | Longest common subsequence | `O(mn)` | `O(n)` | [▶ animation](v1-longest-common-subsequence/animation/index.html) |
