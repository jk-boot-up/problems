# 15. 3Sum — v2: Sort + two pointers

[← Problem statement](../README.md)

> Sort, fix the first number, then find pairs summing to its negative with two pointers, skipping duplicates.

## Approach

**Sort + two pointers.** Sort the array. For each `i` (skipping a value equal to the previous one), search `i+1..n-1` with `l`
and `r` for pairs summing to `-nums[i]`. On a hit, record it and skip equal neighbours on both sides. Stop once
`nums[i] > 0`, because then all three numbers are positive.

* Time: **O(n²)** — n choices of i, each with a linear two-pointer scan (the sort is O(n log n)).
* Space: **O(1)** — apart from sorting and the output.

## Files

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0015/v2/ThreeSum.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0015/v2/ThreeSumTest.java` | JUnit 6 tests |
| `animation/index.html` | Animated walkthrough with spoken narration |

Run the tests with `../gradlew :v2:test`.
