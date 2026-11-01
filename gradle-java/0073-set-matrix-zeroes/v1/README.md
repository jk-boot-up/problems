# 73. Set Matrix Zeroes — v1: Row and column sets

[← Problem statement](../README.md)

> Record which rows and columns contain a zero, then zero them in a second pass.

## Approach

**Two boolean arrays.** `zeroRow[i]` and `zeroCol[j]` are set for every zero. A second pass zeroes a cell if its row or column is flagged.

* Time: **O(m·n)** — two passes.
* Space: **O(m + n)** — the two flag arrays.

## Files

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0073/v1/SetMatrixZeroes.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0073/v1/SetMatrixZeroesTest.java` | JUnit 6 tests |
| `animation/index.html` | Animated walkthrough with spoken narration |

Run the tests with `../gradlew :v1:test`.
