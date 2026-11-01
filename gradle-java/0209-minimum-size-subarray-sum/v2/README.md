# 209. Minimum Size Subarray Sum — v2: Sliding window

[← Problem statement](../README.md)

> Grow the window to the right until the sum reaches the target, then shrink it from the left while it still does.

## Approach

**Sliding window.** Extend `right` and add `nums[right]` to `sum`. While `sum >= target`, record the window length and remove
`nums[left]`, moving `left` forward. All values are positive, so shrinking always lowers the sum.

* Time: **O(n)** — each index enters and leaves the window at most once.
* Space: **O(1)** — the window bounds and the running sum.

## Files

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0209/v2/MinimumSizeSubarraySum.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0209/v2/MinimumSizeSubarraySumTest.java` | JUnit 6 tests |
| `animation/index.html` | Animated walkthrough with spoken narration |

Run the tests with `../gradlew :v2:test`.
