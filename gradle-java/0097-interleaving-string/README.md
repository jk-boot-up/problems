# 97. Interleaving String

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Multidimensional DP &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/interleaving-string/)

## Problem

Return `true` if `s3` is formed by **interleaving** `s1` and `s2`: splitting both into pieces and alternating them, keeping each
string's characters in order.

**Example**
```
s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac" → true
s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc" → false
s1 = "",      s2 = "",      s3 = ""           → true
```

**Constraints**
* `0 <= s1.length, s2.length <= 100`; `0 <= s3.length <= 200`

**Follow-up:** O(s2.length) extra memory.

## Solutions

Each folder below is a separate, self-contained Gradle project, ordered from the simplest idea to the most efficient one.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-2d-dp-table](v1-2d-dp-table/README.md) | 2D DP table | `O(m·n)` | `O(m·n)` | [▶ animation](v1-2d-dp-table/animation/index.html) |
| [v2-1d-dp](v2-1d-dp/README.md) | 1D DP | `O(m·n)` | `O(n)` | [▶ animation](v2-1d-dp/animation/index.html) |
