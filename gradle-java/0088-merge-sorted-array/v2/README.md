# 88. Merge Sorted Array — v2: Three pointers from the back

[← Problem statement](../README.md)

> Fill nums1 from the back with the larger of the two current tails, so nothing unread is overwritten.

## Approach

**Three pointers, writing from the back.** `i` points at the last real value of `nums1`, `j` at the last value of `nums2`,
and `k` at the last slot of `nums1`. At every step copy the larger of `nums1[i]` and `nums2[j]` into `nums1[k]`, then move
the pointer you copied from, and `k`, one step left. Writing from the back means we only ever overwrite slots we have already read.
When `nums2` runs out, the rest of `nums1` is already in place.

* Time: **O(m + n)** — every slot of nums1 is written exactly once.
* Space: **O(1)** — only three index variables.

## Files

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0088/v2/MergeSortedArray.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0088/v2/MergeSortedArrayTest.java` | JUnit 6 tests |
| `animation/index.html` | Animated walkthrough with spoken narration |

Run the tests with `../gradlew :v2:test`.
