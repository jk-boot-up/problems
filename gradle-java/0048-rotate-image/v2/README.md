# 48. Rotate Image — v2: Transpose + reverse rows

[← Problem statement](../README.md)

> A clockwise rotation equals a transpose followed by reversing every row.

## Approach

**Transpose, then mirror.** Swap `a[i][j]` with `a[j][i]` for `j > i` (transpose), then reverse each row.
Element `(i, j)` ends at `(j, n-1-i)`, which is exactly the clockwise rotation.

* Time: **O(n²)** — every cell is swapped a constant number of times.
* Space: **O(1)** — swaps in place.

## Files

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0048/v2/RotateImage.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0048/v2/RotateImageTest.java` | JUnit 6 tests |
| `animation/index.html` | Animated walkthrough with spoken narration |

Run the tests with `../gradlew :v2:test`.
