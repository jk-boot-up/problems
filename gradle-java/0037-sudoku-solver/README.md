# 37. Sudoku Solver

**Difficulty:** Hard &nbsp;|&nbsp; **Topic:** Backtracking &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/sudoku-solver/)

## Problem

Fill the empty cells (`'.'`) of a 9×9 Sudoku so that every row, column and 3×3 box contains `1-9` exactly once. The input has exactly
one solution; modify `board` in place.

**Constraints**
* `board` is 9×9; the puzzle has exactly one solution.

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-backtracking-with-bitmasks](v1-backtracking-with-bitmasks/README.md) | Backtracking with bitmasks | `O(9^E)` | `O(E)` | [▶ animation](v1-backtracking-with-bitmasks/animation/index.html) |
