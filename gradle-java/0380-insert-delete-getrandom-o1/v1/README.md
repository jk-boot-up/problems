# 380. Insert Delete GetRandom O(1) — v1: Optimal

[← Problem statement](../README.md)

> An array gives O(1) random picks; a value→index map gives O(1) lookups; delete by swapping with the last element.

## Approach

**ArrayList + HashMap.** The list stores values so `getRandom` picks a random index. The map stores each value's index.
To remove `val`, move the **last** value into `val`'s slot, update that value's index, and drop the last slot. Nothing shifts.

* Time: **O(1)** — average per operation (hash map + array end operations).
* Space: **O(n)** — the list and the map each hold every stored value.

## Files

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0380/v1/RandomizedSet.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0380/v1/RandomizedSetTest.java` | JUnit 6 tests |
| `animation/index.html` | Animated walkthrough with spoken narration |

Run the tests with `../gradlew :v1:test`.
