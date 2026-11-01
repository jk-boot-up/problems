# 274. H-Index — v1: Sort descending

[← Problem statement](../README.md)

> Sort citations high to low; h grows while the (h+1)-th paper still has more than h citations.

## Approach

**Sort.** Sort ascending and scan from the top: the paper at rank `h + 1` (counting from the most cited) must have at least
`h + 1` citations for the h-index to reach `h + 1`.

* Time: **O(n log n)** — sorting.
* Space: **O(log n)** — the sort's recursion stack.

## Files

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0274/v1/HIndex.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0274/v1/HIndexTest.java` | JUnit 6 tests |
| `animation/index.html` | Animated walkthrough with spoken narration |

Run the tests with `../gradlew :v1:test`.
