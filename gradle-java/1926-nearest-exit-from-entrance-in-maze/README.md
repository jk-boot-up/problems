# 1926. Nearest Exit from Entrance in Maze

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Graph BFS &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/nearest-exit-from-entrance-in-maze/)

## Problem

In a maze of `'.'` (empty) and `'+'` (wall), starting at `entrance`, return the number of steps to the nearest **exit**: an empty cell on the
border that is not the entrance. Return `-1` if none is reachable.

**Example**
```
maze = [["+","+",".","+"],[".",".",".","+"],["+","+","+","."]], entrance = [1,2] → 1
maze = [["+","+","+"],[".",".","."],["+","+","+"]], entrance = [1,0]             → 2
```

**Constraints**
* `1 <= m, n <= 100`

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-bfs-from-the-entrance](v1-bfs-from-the-entrance/README.md) | BFS from the entrance | `O(m·n)` | `O(m·n)` | [▶ animation](v1-bfs-from-the-entrance/animation/index.html) |
