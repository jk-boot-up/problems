# 54. Spiral Matrix — v1: Shrinking boundaries

[← Problem statement](../README.md)

> Peel the matrix layer by layer: walk the top row, right column, bottom row and left column, shrinking the bounds.

## Approach

**Four boundaries.** Keep `top`, `bottom`, `left`, `right`. Walk the top row left→right (`top++`), the right column top→bottom
(`right--`), then, if rows remain, the bottom row right→left (`bottom--`), and if columns remain, the left column bottom→top
(`left++`). Repeat until the bounds cross.

* Time: **O(m·n)** — every cell is visited once.
* Space: **O(1)** — four bounds, apart from the output list.

## Files

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0054/v1/SpiralMatrix.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0054/v1/SpiralMatrixTest.java` | JUnit 6 tests |
| `animation/index.html` | Animated walkthrough with spoken narration |

Run the tests with `../gradlew :v1:test`.
