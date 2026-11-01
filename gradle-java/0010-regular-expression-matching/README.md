# 10. Regular Expression Matching

**Difficulty:** Hard &nbsp;|&nbsp; **Topic:** Multidimensional DP &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/regular-expression-matching/)

## Problem

Implement full-string regular expression matching with `.` (any single character) and `*` (zero or more of the preceding element).

**Example**
```
s = "aa",  p = "a"     → false
s = "aa",  p = "a*"    → true
s = "ab",  p = ".*"    → true
s = "aab", p = "c*a*b" → true
```

**Constraints**
* `1 <= s.length <= 20`; `1 <= p.length <= 20`; every `*` follows a valid character.

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-bottom-up-dp](v1-bottom-up-dp/README.md) | Bottom-up DP | `O(m·n)` | `O(m·n)` | [▶ animation](v1-bottom-up-dp/animation/index.html) |
