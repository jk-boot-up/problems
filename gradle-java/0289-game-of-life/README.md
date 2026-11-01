# 289. Game of Life

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Matrix &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/game-of-life/)

## Problem

The board is an `m × n` grid of cells, each live (`1`) or dead (`0`). Each cell looks at its 8 neighbours and, **all at the
same time**:
1. a live cell with fewer than 2 live neighbours dies;
2. a live cell with 2 or 3 live neighbours lives on;
3. a live cell with more than 3 live neighbours dies;
4. a dead cell with exactly 3 live neighbours becomes live.

Update `board` in place to the next state.

**Example**
```
Input:  [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
Output: [[0,0,0],[1,0,1],[0,1,1],[0,1,0]]
```

**Constraints**
* `1 <= m, n <= 25`

**Follow-up:** solve it in place.

## Solutions

Each folder below is a separate, self-contained Gradle project, ordered from the simplest idea to the most efficient one.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-copy-of-the-board](v1-copy-of-the-board/README.md) | Copy of the board | `O(m·n)` | `O(m·n)` | [▶ animation](v1-copy-of-the-board/animation/index.html) |
| [v2-in-place-two-bit-states](v2-in-place-two-bit-states/README.md) | In-place two-bit states | `O(m·n)` | `O(1)` | [▶ animation](v2-in-place-two-bit-states/animation/index.html) |
