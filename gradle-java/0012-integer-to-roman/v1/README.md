# 12. Integer to Roman — v1: Optimal

[← Problem statement](../README.md)

> Greedy: repeatedly take the largest value (including the six subtractive pairs) that still fits.

## Approach

**Greedy table.** Use a table of 13 values in descending order: `1000 M, 900 CM, 500 D, 400 CD, 100 C, 90 XC, 50 L, 40 XL, 10 X, 9 IX, 5 V, 4 IV, 1 I`.
While `num` is at least the current value, append its symbol and subtract.

* Time: **O(1)** — the output is at most 15 symbols, because num ≤ 3999.
* Space: **O(1)** — the fixed table and the output builder.

## Files

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0012/v1/IntegerToRoman.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0012/v1/IntegerToRomanTest.java` | JUnit 6 tests |
| `animation/index.html` | Animated walkthrough with spoken narration |

Run the tests with `../gradlew :v1:test`.
