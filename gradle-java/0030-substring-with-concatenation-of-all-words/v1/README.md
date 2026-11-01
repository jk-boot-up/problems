# 30. Substring with Concatenation of All Words — v1: Check every start

[← Problem statement](../README.md)

> For each start index, cut k words and compare their counts with the required counts.

## Approach

**Brute force.** For each start `i` with room for `k` words, read the `k` consecutive chunks of length `L` and count them;
stop early when a chunk is not needed or is seen too often.

* Time: **O(n·k·L)** — n starts × k words × L characters to cut each word.
* Space: **O(k)** — the per-start count map.

## Files

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0030/v1/SubstringConcatenation.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0030/v1/SubstringConcatenationTest.java` | JUnit 6 tests |
| `animation/index.html` | Animated walkthrough with spoken narration |

Run the tests with `../gradlew :v1:test`.
