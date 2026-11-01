# 132. Palindrome Partitioning II

**Difficulty:** Hard &nbsp;|&nbsp; **Topic:** Multidimensional DP &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/palindrome-partitioning-ii/)

## Problem

Return the minimum number of cuts needed to partition `s` so that every piece is a palindrome.

**Example**
```
"aab" → 1 ("aa" | "b"),   "a" → 0,   "ab" → 1
```

**Constraints**
* `1 <= s.length <= 2000`

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-centre-expansion-cut-dp](v1-centre-expansion-cut-dp/README.md) | Centre expansion + cut DP | `O(n²)` | `O(n)` | [▶ animation](v1-centre-expansion-cut-dp/animation/index.html) |
