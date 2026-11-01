# 167. Two Sum II - Input Array Is Sorted — v1: Binary search for the partner

[← Problem statement](../README.md)

> For each value, binary-search the rest of the sorted array for target minus that value.

## Approach

**Binary search.** For every `i`, search `numbers[i+1..n-1]` for `target - numbers[i]`.

* Time: **O(n log n)** — n binary searches.
* Space: **O(1)** — a few indices.

## Files

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0167/v1/TwoSumII.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0167/v1/TwoSumIITest.java` | JUnit 6 tests |
| `animation/index.html` | Animated walkthrough with spoken narration |

Run the tests with `../gradlew :v1:test`.
