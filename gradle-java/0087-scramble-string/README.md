# 87. Scramble String

**Difficulty:** Hard &nbsp;|&nbsp; **Topic:** Multidimensional DP &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/scramble-string/)

## Problem

A string is scrambled by splitting it into two non-empty parts, optionally swapping them, and scrambling each part recursively. Return
`true` if `s2` is a scrambled string of `s1`.

**Example**
```
"great", "rgeat" → true,   "abcde", "caebd" → false,   "a", "a" → true
```

**Constraints**
* `1 <= s1.length <= 30`; `s2.length == s1.length`

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-memoized-recursion-with-pruning](v1-memoized-recursion-with-pruning/README.md) | Memoized recursion with pruning | `O(n⁴)` | `O(n³)` | [▶ animation](v1-memoized-recursion-with-pruning/animation/index.html) |
