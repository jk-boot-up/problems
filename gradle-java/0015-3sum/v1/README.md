# 15. 3Sum — v1: Hash set per fixed number

[← Problem statement](../README.md)

> Fix nums[i]; scan the rest with a hash set looking for the value that completes the triplet.

## Approach

**Hashing.** Sort (so triplets come out in a canonical order), then for each `i` scan `j > i` with a set of seen values:
if `-(nums[i] + nums[j])` was seen, record the triplet. A `Set<List<Integer>>` removes duplicates.

* Time: **O(n²)** — n fixed values × a linear scan.
* Space: **O(n)** — the seen set (plus the output).

## Files

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0015/v1/ThreeSum.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0015/v1/ThreeSumTest.java` | JUnit 6 tests |
| `animation/index.html` | Animated walkthrough with spoken narration |

Run the tests with `../gradlew :v1:test`.
