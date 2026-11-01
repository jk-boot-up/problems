# 73. Set Matrix Zeroes — v2: Markers in row/column 0

[← Problem statement](../README.md)

> Use the first row and first column as the zero markers, with two flags for the first row and column themselves.

## Approach

**Reuse the first row and column.** First remember whether row 0 and column 0 contain a zero. Then, for every zero at `(i, j)`
with `i, j >= 1`, mark `matrix[i][0] = 0` and `matrix[0][j] = 0`. Zero every inner cell whose row or column is marked. Finally
zero row 0 and column 0 if their flags are set.

* Time: **O(m·n)** — a few passes over the matrix.
* Space: **O(1)** — two boolean flags.

## Files

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0073/v2/SetMatrixZeroes.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0073/v2/SetMatrixZeroesTest.java` | JUnit 6 tests |
| `animation/index.html` | Animated walkthrough with spoken narration |

Run the tests with `../gradlew :v2:test`.
