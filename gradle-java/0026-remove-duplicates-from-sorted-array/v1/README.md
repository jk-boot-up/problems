# 26. Remove Duplicates from Sorted Array — v1: Optimal

[← Problem statement](../README.md)

> In a sorted array, a value is new exactly when it differs from the last value we kept.

## Approach

**Two pointers.** `k` is the length of the unique prefix (starts at 1). For each `i` from 1, if `nums[i] != nums[k-1]` it is a
new value, so write it to `nums[k]` and grow `k`.

* Time: **O(n)** — each element is looked at once.
* Space: **O(1)** — duplicates are overwritten in place.

## Files

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0026/v1/RemoveDuplicates.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0026/v1/RemoveDuplicatesTest.java` | JUnit 6 tests |
| `animation/index.html` | Animated walkthrough with spoken narration |

Run the tests with `../gradlew :v1:test`.
