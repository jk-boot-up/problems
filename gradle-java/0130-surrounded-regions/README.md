# 130. Surrounded Regions

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Graph General &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/surrounded-regions/)

## Problem

Given an `m × n` board of `'X'` and `'O'`, capture every region of `'O'` that is **completely surrounded** by `'X'` (connected
horizontally or vertically) by flipping it to `'X'`. Regions touching the border are not surrounded.

**Example**
```
Input:          Output:
X X X X         X X X X
X O O X         X X X X
X X O X         X X X X
X O X X         X O X X
```

**Constraints**
* `1 <= m, n <= 200`

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-flood-fill-from-the-border](v1-flood-fill-from-the-border/README.md) | Flood fill from the border | `O(m·n)` | `O(m·n)` | [▶ animation](v1-flood-fill-from-the-border/animation/index.html) |
