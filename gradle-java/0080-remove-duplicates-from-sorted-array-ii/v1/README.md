# 80. Remove Duplicates from Sorted Array II — v1: Optimal

[← Problem statement](../README.md)

> Keep a value only if it differs from the value two slots back in the kept prefix.

## Approach

**Compare with two back.** Keep a write index `k`. A value `x` may be written if `k < 2` or `x != nums[k - 2]`. If it equals
`nums[k-2]`, then because the array is sorted, `nums[k-2]` and `nums[k-1]` are both `x` already, so writing it would make a third copy.

* Time: **O(n)** — a single pass.
* Space: **O(1)** — in-place overwrite with one write index.

## Files

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0080/v1/RemoveDuplicatesII.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0080/v1/RemoveDuplicatesIITest.java` | JUnit 6 tests |
| `animation/index.html` | Animated walkthrough with spoken narration |

Run the tests with `../gradlew :v1:test`.
