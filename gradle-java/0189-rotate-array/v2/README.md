# 189. Rotate Array — v2: Triple reversal

[← Problem statement](../README.md)

> Rotate right by k with three reversals: the whole array, then the first k, then the rest.

## Approach

**Triple reversal.** Let `k = k % n`. Reverse the whole array: the last `k` values move to the front, but in reverse order.
Then reverse the first `k` values and the remaining `n - k` values to restore their order.

* Time: **O(n)** — every element is swapped at most twice.
* Space: **O(1)** — swaps happen in place.

## Files

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0189/v2/RotateArray.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0189/v2/RotateArrayTest.java` | JUnit 6 tests |
| `animation/index.html` | Animated walkthrough with spoken narration |

Run the tests with `../gradlew :v2:test`.
