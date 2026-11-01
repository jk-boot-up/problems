# 36. Valid Sudoku — v1: Seen sets in one pass

[← Problem statement](../README.md)

> One pass over the cells, remembering each digit per row, per column and per 3×3 box.

## Approach

**Boolean tables.** Keep `rows[9][9]`, `cols[9][9]` and `boxes[9][9]`. For each digit `d` at `(r, c)`, the box index is
`(r / 3) * 3 + c / 3`. If any of the three tables already marks `d`, the board is invalid; otherwise mark it.

* Time: **O(1)** — the board is always 81 cells.
* Space: **O(1)** — three fixed 9×9 tables.

## Files

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0036/v1/ValidSudoku.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0036/v1/ValidSudokuTest.java` | JUnit 6 tests |
| `animation/index.html` | Animated walkthrough with spoken narration |

Run the tests with `../gradlew :v1:test`.
