# 419. Battleships in a Board

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Matrix &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/battleships-in-a-board/)

## Problem

A board of `'X'` (ship) and `'.'` (water) holds straight horizontal or vertical ships, never touching each other. Count the ships in one
pass, using O(1) extra memory and without modifying the board.

**Example**
```
X . . X
. . . X    → 2
. . . X
```

**Constraints**
* `1 <= m, n <= 200`

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-count-ship-heads](v1-count-ship-heads/README.md) | Count ship heads | `O(mn)` | `O(1)` | [▶ animation](v1-count-ship-heads/animation/index.html) |
