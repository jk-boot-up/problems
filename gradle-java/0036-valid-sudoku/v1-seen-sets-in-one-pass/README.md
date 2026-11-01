# 36. Valid Sudoku — v1: Seen sets in one pass

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

## Approach: Seen sets in one pass

> One pass over the cells, remembering each digit per row, per column and per 3×3 box.

**Boolean tables.** Keep `rows[9][9]`, `cols[9][9]` and `boxes[9][9]`. For each digit `d` at `(r, c)`, the box index is
`(r / 3) * 3 + c / 3`. If any of the three tables already marks `d`, the board is invalid; otherwise mark it.

* Time: **O(1)** — the board is always 81 cells.
* Space: **O(1)** — three fixed 9×9 tables.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0036/v1/ValidSudoku.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0036/v1/ValidSudokuTest.java` | JUnit 6 tests |
| `animation/index.html` | Animated walkthrough with spoken narration |

## Build and test

This folder is a standalone Gradle 9.8.2 project. Only a JDK is needed to start Gradle; JDK 25 is downloaded
automatically if it is missing.

```bash
./gradlew test
```

## Animation

Open [`animation/index.html`](animation/index.html) in a browser. It has three tabs:

* **Problem:** the statement and the key idea.
* **Walkthrough:** pick a scenario and press **Play**. Each step is animated and read aloud by your browser's speech
  engine (untick *Narration* to mute). Keys: space = play/pause, ← / → = step, 1–9 = scenario.
* **Complexity:** time and space cost, plotted against the common growth curves.

Switch between Light, Medium and Dark themes in the header.
