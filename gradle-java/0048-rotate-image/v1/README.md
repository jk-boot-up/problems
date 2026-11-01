# 48. Rotate Image — v1: Copy into a new matrix

[← Problem statement](../README.md)

> Cell (i, j) moves to (j, n−1−i); fill a copy, then copy it back.

## Approach

**Extra matrix.** Write `rotated[j][n-1-i] = matrix[i][j]` for every cell, then copy `rotated` back row by row.
Easy to reason about, but it breaks the in-place requirement.

* Time: **O(n²)** — each cell is copied twice.
* Space: **O(n²)** — the second matrix.

## Files

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0048/v1/RotateImage.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0048/v1/RotateImageTest.java` | JUnit 6 tests |
| `animation/index.html` | Animated walkthrough with spoken narration |

Run the tests with `../gradlew :v1:test`.
