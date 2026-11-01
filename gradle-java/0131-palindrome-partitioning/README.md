# 131. Palindrome Partitioning

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Backtracking &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/palindrome-partitioning/)

## Problem

Partition `s` so that every piece is a palindrome. Return all such partitions.

**Example**
```
"aab" → [["a","a","b"],["aa","b"]]
```

**Constraints**
* `1 <= s.length <= 16`; lowercase letters.

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-backtracking-over-prefixes](v1-backtracking-over-prefixes/README.md) | Backtracking over prefixes | `O(n · 2ⁿ)` | `O(n)` | [▶ animation](v1-backtracking-over-prefixes/animation/index.html) |
