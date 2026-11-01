# 169. Majority Element — v2: Sort and take the middle

[← Problem statement](../README.md)

> After sorting, the majority value always covers the middle index.

## Approach

**Sort.** A value that fills more than half of the array must cover index `n / 2` once sorted.

* Time: **O(n log n)** — sorting.
* Space: **O(log n)** — the sort's recursion stack.

## Files

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0169/v2/MajorityElement.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0169/v2/MajorityElementTest.java` | JUnit 6 tests |
| `animation/index.html` | Animated walkthrough with spoken narration |

Run the tests with `../gradlew :v2:test`.
