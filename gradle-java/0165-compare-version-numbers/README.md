# 165. Compare Version Numbers

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Two Pointers &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/compare-version-numbers/)

## Problem

Compare two version strings made of revisions separated by dots. Revisions compare as integers (leading zeros ignored); a missing revision
counts as 0. Return `-1`, `0` or `1`.

**Example**
```
"1.2", "1.10" → -1,   "1.01", "1.001" → 0,   "1.0", "1.0.0.0" → 0
```

**Constraints**
* `1 <= length <= 500`; revisions fit in 32 bits.

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-revision-wise-parsing](v1-revision-wise-parsing/README.md) | Revision-wise parsing | `O(m + n)` | `O(1)` | [▶ animation](v1-revision-wise-parsing/animation/index.html) |
