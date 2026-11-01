# 1791. Find Center of Star Graph

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Graph &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/find-center-of-star-graph/)

## Problem

An undirected **star** graph has one centre connected to every other node, and no other edges. Given its edges, return the centre.

**Example**
```
[[1,2],[2,3],[4,2]]       → 2
[[1,2],[5,1],[1,3],[1,4]] → 1
```

**Constraints**
* `3 <= n <= 10^5`; the input is a valid star

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-compare-two-edges](v1-compare-two-edges/README.md) | Compare two edges | `O(1)` | `O(1)` | [▶ animation](v1-compare-two-edges/animation/index.html) |
