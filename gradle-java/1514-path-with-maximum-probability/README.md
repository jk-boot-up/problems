# 1514. Path with Maximum Probability

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Shortest Path &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/path-with-maximum-probability/)

## Problem

An undirected graph has `n` nodes; edge `edges[i]` succeeds with probability `succProb[i]`. Return the highest probability of a path from
`start` to `end` (the product of its edges), or 0 if there is none.

**Example**
```
n = 3, edges = [[0,1],[1,2],[0,2]], succProb = [0.5,0.5,0.2], start = 0, end = 2 → 0.25
n = 3, edges = [[0,1],[1,2],[0,2]], succProb = [0.5,0.5,0.3], start = 0, end = 2 → 0.3
```

**Constraints**
* `2 <= n <= 10^4`, up to `2 * 10^4` edges, `0 <= succProb[i] <= 1`

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-dijkstra-with-a-max-heap](v1-dijkstra-with-a-max-heap/README.md) | Dijkstra with a max-heap | `O((V + E) log V)` | `O(V + E)` | [▶ animation](v1-dijkstra-with-a-max-heap/animation/index.html) |
