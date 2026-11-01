# 95. Unique Binary Search Trees II

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Backtracking &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/unique-binary-search-trees-ii/)

## Problem

Return all structurally unique BSTs that store exactly the values `1..n`, in any order.

**Example**
```
n = 3 → 5 trees: [1,null,2,null,3], [1,null,3,2], [2,1,3], [3,1,null,null,2], [3,2,null,1]
```

**Constraints**
* `1 <= n <= 8`

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-recursive-generation](v1-recursive-generation/README.md) | Recursive generation | `O(n · Cₙ)` | `O(n · Cₙ)` | [▶ animation](v1-recursive-generation/animation/index.html) |
