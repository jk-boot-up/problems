# 417. Pacific Atlantic Water Flow

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Graph General &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/pacific-atlantic-water-flow/)

## Problem

Rain flows from a cell to a 4-directional neighbour of **equal or lower** height. The Pacific touches the top and left edges, the
Atlantic the bottom and right edges. Return all cells from which water can reach **both** oceans.

**Example**
```
heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
→ [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
```

**Constraints**
* `1 <= m, n <= 200`

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-reverse-bfs-from-both-oceans](v1-reverse-bfs-from-both-oceans/README.md) | Reverse BFS from both oceans | `O(m·n)` | `O(m·n)` | [▶ animation](v1-reverse-bfs-from-both-oceans/animation/index.html) |
