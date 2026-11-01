# 289. Game of Life — v2: In-place two-bit states

[← Problem statement](../README.md)

> Update in place by encoding both the old and new state in each cell (bit 0 = now, bit 1 = next).

## Approach

**Two bits per cell.** Bit 0 is the current state, bit 1 the next state. Count live neighbours using `cell & 1`, so cells
already updated still report their old state. Set bit 1 when the cell lives next round. Finally shift every cell right by one.

* Time: **O(m·n)** — 8 neighbour checks per cell.
* Space: **O(1)** — the board stores both generations.

## Files

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0289/v2/GameOfLife.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0289/v2/GameOfLifeTest.java` | JUnit 6 tests |
| `animation/index.html` | Animated walkthrough with spoken narration |

Run the tests with `../gradlew :v2:test`.
