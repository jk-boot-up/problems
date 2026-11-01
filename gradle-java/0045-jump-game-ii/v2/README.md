# 45. Jump Game II — v2: Greedy windows

[← Problem statement](../README.md)

> Breadth-first in disguise: each jump covers a window of indices; the next window ends at the farthest reach from it.

## Approach

**Greedy levels.** All indices reachable with `j` jumps form a window ending at `end`. While scanning that window, track
`farthest = max(i + nums[i])`. When `i` reaches `end`, we must take another jump: `jumps++`, `end = farthest`.

* Time: **O(n)** — every index is scanned once across all windows.
* Space: **O(1)** — three counters.

## Files

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0045/v2/JumpGameII.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0045/v2/JumpGameIITest.java` | JUnit 6 tests |
| `animation/index.html` | Animated walkthrough with spoken narration |

Run the tests with `../gradlew :v2:test`.
