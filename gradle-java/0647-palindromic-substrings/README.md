# 647. Palindromic Substrings

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Two Pointers &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/palindromic-substrings/)

## Problem

Return how many substrings of `s` are palindromes (substrings at different positions count separately).

**Example**
```
"abc" → 3,   "aaa" → 6
```

**Constraints**
* `1 <= s.length <= 1000`

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-expand-around-centres](v1-expand-around-centres/README.md) | Expand around centres | `O(n²)` | `O(1)` | [▶ animation](v1-expand-around-centres/animation/index.html) |
