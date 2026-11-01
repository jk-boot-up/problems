# 36. Valid Sudoku

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Matrix &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/valid-sudoku/)

## Problem

Decide whether a partially filled 9×9 Sudoku board is **valid**. Only the filled cells need to follow the rules:
* each row has the digits `1-9` at most once,
* each column has the digits `1-9` at most once,
* each of the nine 3×3 boxes has the digits `1-9` at most once.

Empty cells are `'.'`. A valid board does not need to be solvable.

**Example**
```
Input: the classic example board (rows "53..7....", "6..195...", ...)
Output: true
Changing the top-left 5 to 8 makes column 0 contain 8 twice → false
```

**Constraints**
* `board` is 9×9; each cell is a digit `1-9` or `'.'`.

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-seen-sets-in-one-pass](v1-seen-sets-in-one-pass/README.md) | Seen sets in one pass | `O(1)` | `O(1)` | [▶ animation](v1-seen-sets-in-one-pass/animation/index.html) |
