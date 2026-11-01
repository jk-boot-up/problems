# 1424. Diagonal Traverse II

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Matrix &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/diagonal-traverse-ii/)

## Problem

Given a jagged 2-D list `nums` (rows may have different lengths), return all elements in diagonal order: anti-diagonals `i + j = 0, 1, 2,
…`, each read from bottom-left to top-right.

**Example**
```
[[1,2,3],[4,5,6],[7,8,9]] → [1,4,2,7,5,3,8,6,9]
[[1,2,3,4,5],[6,7],[8],[9,10,11],[12,13,14,15,16]] → [1,6,2,8,7,3,9,4,12,10,5,13,11,14,15,16]
```

**Constraints**
* Up to `10^5` elements in total

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-buckets-by-i-j](v1-buckets-by-i-j/README.md) | Buckets by i + j | `O(N)` | `O(N)` | [▶ animation](v1-buckets-by-i-j/animation/index.html) |
