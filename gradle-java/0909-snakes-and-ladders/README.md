# 909. Snakes and Ladders

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Graph BFS &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/snakes-and-ladders/)

## Problem

An `n × n` board is numbered `1..n²` in a **boustrophedon** pattern starting at the bottom-left (row direction alternates). From
square `cur`, a die roll moves you to any of `cur+1 .. min(cur+6, n²)`. If that square has `board[r][c] != -1`, you must take the
snake or ladder to that square (only one per move). Return the fewest rolls to reach `n²`, or `-1`.

**Example**
```
Input:  board = [[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],
                 [-1,35,-1,-1,13,-1],[-1,-1,-1,-1,-1,-1],[-1,15,-1,-1,-1,-1]]
Output: 4
```

**Constraints**
* `2 <= n <= 20`; squares 1 and n² have no snake or ladder.

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-bfs-over-squares](v1-bfs-over-squares/README.md) | BFS over squares | `O(n²)` | `O(n²)` | [▶ animation](v1-bfs-over-squares/animation/index.html) |
