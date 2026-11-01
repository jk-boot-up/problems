# 14. Longest Common Prefix — v1: Optimal

[← Problem statement](../README.md)

> Compare column by column: the prefix grows until some string ends or differs in that column.

## Approach

**Vertical scan.** For column `c = 0, 1, …`, check that every string has a character at `c` equal to `strs[0].charAt(c)`.
Stop at the first mismatch or end of a string; the prefix is `strs[0].substring(0, c)`.

* Time: **O(S)** — S is the total number of characters; each is compared at most once.
* Space: **O(1)** — apart from the returned substring.

## Files

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0014/v1/LongestCommonPrefix.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0014/v1/LongestCommonPrefixTest.java` | JUnit 6 tests |
| `animation/index.html` | Animated walkthrough with spoken narration |

Run the tests with `../gradlew :v1:test`.
