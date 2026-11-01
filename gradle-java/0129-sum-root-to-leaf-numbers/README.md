# 129. Sum Root to Leaf Numbers

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Binary Tree General &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/sum-root-to-leaf-numbers/)

## Problem

Every node holds a digit `0-9`. Each root-to-leaf path forms a number (e.g. `1 → 2 → 3` is `123`). Return the sum of all
these numbers.

**Example 1**
```
Input:  [1,2,3]
Output: 25   (12 + 13)
```

**Example 2**
```
Input:  [4,9,0,5,1]
Output: 1026   (495 + 491 + 40)
```

**Constraints**
* `1 <= n <= 1000`; depth at most 10; answer fits in 32 bits.

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-dfs-carrying-the-number](v1-dfs-carrying-the-number/README.md) | DFS carrying the number | `O(n)` | `O(h)` | [▶ animation](v1-dfs-carrying-the-number/animation/index.html) |
