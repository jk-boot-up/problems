# 167. Two Sum II - Input Array Is Sorted — v2: Two pointers

[← Problem statement](../README.md)

> Sorted input: if the sum is too small move the left pointer right, if too big move the right pointer left.

## Approach

**Two pointers.** Start `l = 0`, `r = n - 1`. If `numbers[l] + numbers[r]` is too small, only a larger left value can help,
so `l++`; if too big, `r--`. Each move rules out a value that can't be part of the answer.

* Time: **O(n)** — the pointers move toward each other at most n times.
* Space: **O(1)** — two indices.

## Files

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0167/v2/TwoSumII.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0167/v2/TwoSumIITest.java` | JUnit 6 tests |
| `animation/index.html` | Animated walkthrough with spoken narration |

Run the tests with `../gradlew :v2:test`.
