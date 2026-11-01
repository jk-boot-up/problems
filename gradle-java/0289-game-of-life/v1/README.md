# 289. Game of Life — v1: Copy of the board

[← Problem statement](../README.md)

> Read neighbours from an untouched copy and write the new states into the board.

## Approach

**Snapshot.** Copy the board; count neighbours in the copy and write each cell's next state into the original.

* Time: **O(m·n)** — 8 neighbour checks per cell.
* Space: **O(m·n)** — the copy.

## Files

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0289/v1/GameOfLife.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0289/v1/GameOfLifeTest.java` | JUnit 6 tests |
| `animation/index.html` | Animated walkthrough with spoken narration |

Run the tests with `../gradlew :v1:test`.
