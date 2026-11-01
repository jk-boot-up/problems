# 13. Roman to Integer — v1: Optimal

[← Problem statement](../README.md)

> Add each symbol's value, but subtract it when a larger symbol follows (IV, IX, XL, ...).

## Approach

**Look one ahead.** For each symbol, if the next symbol is larger, this one is subtracted; otherwise it is added.

* Time: **O(n)** — one pass over the string.
* Space: **O(1)** — a fixed symbol table.

## Files

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0013/v1/RomanToInteger.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0013/v1/RomanToIntegerTest.java` | JUnit 6 tests |
| `animation/index.html` | Animated walkthrough with spoken narration |

Run the tests with `../gradlew :v1:test`.
