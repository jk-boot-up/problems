# 1672. Richest Customer Wealth

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Matrix &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/richest-customer-wealth/)

## Problem

`accounts[i][j]` is the money customer `i` has in bank `j`. Return the wealth (row total) of the richest customer.

**Example**
```
[[1,2,3],[3,2,1]]      → 6
[[1,5],[7,3],[3,5]]    → 10
```

**Constraints**
* `1 <= m, n <= 50`

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-row-sums](v1-row-sums/README.md) | Row sums | `O(mn)` | `O(1)` | [▶ animation](v1-row-sums/animation/index.html) |
