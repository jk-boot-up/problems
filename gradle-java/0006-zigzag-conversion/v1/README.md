# 6. Zigzag Conversion — v1: Optimal

[← Problem statement](../README.md)

> Deal characters onto rows, bouncing the row index down and up; then read the rows in order.

## Approach

**Simulate the rows.** Keep one `StringBuilder` per row and a current row with a direction. Append each character to the
current row; flip direction at the top and bottom rows. Concatenate the rows. With one row, return `s`.

* Time: **O(n)** — each character is placed once and read once.
* Space: **O(n)** — the row builders hold every character.

## Files

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0006/v1/ZigzagConversion.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0006/v1/ZigzagConversionTest.java` | JUnit 6 tests |
| `animation/index.html` | Animated walkthrough with spoken narration |

Run the tests with `../gradlew :v1:test`.
