# 209. Minimum Size Subarray Sum — v1: Prefix sums + binary search

[← Problem statement](../README.md)

> With prefix sums, for each start binary-search the first end whose window sum reaches the target.

## Approach

**Prefix sums.** `pre[i]` = sum of the first `i` values (increasing, since all values are positive). For each `i`,
binary-search the smallest `j` with `pre[j] - pre[i] >= target`; the window length is `j - i`.

* Time: **O(n log n)** — n binary searches.
* Space: **O(n)** — the prefix-sum array.

## Files

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0209/v1/MinimumSizeSubarraySum.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0209/v1/MinimumSizeSubarraySumTest.java` | JUnit 6 tests |
| `animation/index.html` | Animated walkthrough with spoken narration |

Run the tests with `../gradlew :v1:test`.
