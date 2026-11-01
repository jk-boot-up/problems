# 274. H-Index — v2: Counting buckets

[← Problem statement](../README.md)

> Count papers by citation (capped at n), then walk down from n until at least h papers have h or more citations.

## Approach

**Counting sort.** The answer is at most `n`, so put every paper into a bucket `min(c, n)`. Walk `h` from `n` down to 0,
keeping a running total of papers with at least `h` citations. The first `h` where that total reaches `h` is the answer.

* Time: **O(n)** — one pass to fill buckets, one pass down them.
* Space: **O(n)** — the bucket array of size n + 1.

## Files

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0274/v2/HIndex.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0274/v2/HIndexTest.java` | JUnit 6 tests |
| `animation/index.html` | Animated walkthrough with spoken narration |

Run the tests with `../gradlew :v2:test`.
