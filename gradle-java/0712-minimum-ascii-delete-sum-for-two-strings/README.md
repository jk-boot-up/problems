# 712. Minimum ASCII Delete Sum for Two Strings

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Dynamic Programming &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/minimum-ascii-delete-sum-for-two-strings/)

## Problem

Return the lowest total ASCII value of characters deleted from `s1` and `s2` to make the two strings equal.

**Example**
```
"sea", "eat"      → 231   (delete 's' = 115 and 't' = 116)
"delete", "leet"  → 403
```

**Constraints**
* `1 <= length <= 1000`, lower-case letters

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-dp-over-suffixes](v1-dp-over-suffixes/README.md) | DP over suffixes | `O(mn)` | `O(n)` | [▶ animation](v1-dp-over-suffixes/animation/index.html) |
