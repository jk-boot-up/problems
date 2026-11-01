# 27. Remove Element — v1: Optimal

[← Problem statement](../README.md)

> A write pointer keeps every value that is not val; the reader skips the ones that are.

## Approach

**Read/write pointers.** Scan the array with a reader `i`. Whenever `nums[i] != val`, copy it to `nums[k]` and advance `k`.
At the end, `k` is the number of kept values and they sit at the front.

* Time: **O(n)** — one pass over the array.
* Space: **O(1)** — the array is rewritten in place.

## Files

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0027/v1/RemoveElement.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0027/v1/RemoveElementTest.java` | JUnit 6 tests |
| `animation/index.html` | Animated walkthrough with spoken narration |

Run the tests with `../gradlew :v1:test`.
