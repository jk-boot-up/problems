# 169. Majority Element — v1: Hash map counting

[← Problem statement](../README.md)

> Count every value in a hash map; return the first one whose count passes n / 2.

## Approach

**Count occurrences.** Increment `count[x]` for each value; as soon as a count exceeds `n / 2`, that value is the answer.

* Time: **O(n)** — one pass with O(1) map updates.
* Space: **O(n)** — up to n distinct keys in the map.

## Files

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0169/v1/MajorityElement.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0169/v1/MajorityElementTest.java` | JUnit 6 tests |
| `animation/index.html` | Animated walkthrough with spoken narration |

Run the tests with `../gradlew :v1:test`.
