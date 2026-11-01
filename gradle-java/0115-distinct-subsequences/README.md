# 115. Distinct Subsequences

**Difficulty:** Hard &nbsp;|&nbsp; **Topic:** Multidimensional DP &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/distinct-subsequences/)

## Problem

Return the number of distinct **subsequences** of `s` that equal `t` (the answer fits in 32 bits).

**Example**
```
s = "rabbbit", t = "rabbit" → 3
s = "babgbag", t = "bag"    → 5
```

**Constraints**
* `1 <= s.length, t.length <= 1000`

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-1d-dp](v1-1d-dp/README.md) | 1D DP | `O(m·n)` | `O(n)` | [▶ animation](v1-1d-dp/animation/index.html) |
