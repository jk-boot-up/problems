# 44. Wildcard Matching

**Difficulty:** Hard &nbsp;|&nbsp; **Topic:** Multidimensional DP &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/wildcard-matching/)

## Problem

Implement full-string wildcard matching where `?` matches any single character and `*` matches any sequence (including empty).

**Example**
```
s = "aa", p = "a"    → false
s = "aa", p = "*"    → true
s = "cb", p = "?a"   → false
s = "adceb", p = "*a*b" → true
```

**Constraints**
* `0 <= s.length, p.length <= 2000`

## Solutions

Each folder below is a separate, self-contained Gradle project, ordered from the simplest idea to the most efficient one.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-dp-table](v1-dp-table/README.md) | DP table | `O(m·n)` | `O(m·n)` | [▶ animation](v1-dp-table/animation/index.html) |
| [v2-greedy-with-star-backtracking](v2-greedy-with-star-backtracking/README.md) | Greedy with star backtracking | `O(m·n)` | `O(1)` | [▶ animation](v2-greedy-with-star-backtracking/animation/index.html) |
