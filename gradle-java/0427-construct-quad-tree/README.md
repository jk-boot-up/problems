# 427. Construct Quad-Tree

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Divide & Conquer &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/construct-quad-tree/)

## Problem

Given an `n × n` grid of `0`s and `1`s (`n` a power of two), build its **quad tree**. Each node has `val`, `isLeaf` and four children
(`topLeft`, `topRight`, `bottomLeft`, `bottomRight`). A uniform region is a leaf whose `val` is that value; any other region is an
internal node (its `val` may be anything) whose four children represent its four equal quadrants.

**Example**
```
Input:  grid = [[0,1],[1,0]]
Output: an internal node with four leaves 0, 1, 1, 0
```

**Constraints**
* `n == 2^x` with `0 <= x <= 6`

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-recursive-quadrants](v1-recursive-quadrants/README.md) | Recursive quadrants | `O(n²)` | `O(log n)` | [▶ animation](v1-recursive-quadrants/animation/index.html) |
