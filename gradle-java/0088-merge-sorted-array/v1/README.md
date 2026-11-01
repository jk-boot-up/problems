# 88. Merge Sorted Array — v1: Copy and sort

[← Problem statement](../README.md)

> Copy nums2 into the empty tail of nums1, then sort the whole array.

## Approach

**Copy, then sort.** The last `n` slots of `nums1` are free, so copy `nums2` there and call `Arrays.sort`.
Simple and correct, but it ignores that both inputs are already sorted.

* Time: **O((m + n) log(m + n))** — the sort dominates.
* Space: **O(log(m + n))** — the recursion stack of the sort on primitives.

## Files

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0088/v1/MergeSortedArray.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0088/v1/MergeSortedArrayTest.java` | JUnit 6 tests |
| `animation/index.html` | Animated walkthrough with spoken narration |

Run the tests with `../gradlew :v1:test`.
