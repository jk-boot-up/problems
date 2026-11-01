# 1143. Longest Common Subsequence

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Multidimensional DP &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/longest-common-subsequence/)

## Problem

Return the length of the longest **common subsequence** of `text1` and `text2` (0 if none).

**Example**
```
"abcde", "ace" → 3,   "abc", "abc" → 3,   "abc", "def" → 0
```

**Constraints**
* `1 <= text1.length, text2.length <= 1000`

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-2d-dp-table](v1-2d-dp-table/README.md) | 2D DP table | `O(m·n)` | `O(m·n)` | [▶ animation](v1-2d-dp-table/animation/index.html) |
