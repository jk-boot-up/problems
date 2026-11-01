# 96. Unique Binary Search Trees

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** 1D DP &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/unique-binary-search-trees/)

## Problem

Return the number of structurally unique BSTs that store exactly the values `1..n`.

**Example**
```
n = 3 → 5,   n = 1 → 1
```

**Constraints**
* `1 <= n <= 19`

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-catalan-dp](v1-catalan-dp/README.md) | Catalan DP | `O(n²)` | `O(n)` | [▶ animation](v1-catalan-dp/animation/index.html) |
