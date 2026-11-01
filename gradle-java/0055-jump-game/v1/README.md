# 55. Jump Game — v1: Optimal

[← Problem statement](../README.md)

> Track the farthest index reachable so far; if you ever stand beyond it, you are stuck.

## Approach

**Greedy reach.** Keep `reach`, the farthest index reachable so far. Walk `i` left to right. If `i > reach` you can't get here,
so return `false`. Otherwise update `reach = max(reach, i + nums[i])`. Return `true` once `reach` covers the last index.

* Time: **O(n)** — each index is visited at most once.
* Space: **O(1)** — a single reach variable.

## Files

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0055/v1/JumpGame.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0055/v1/JumpGameTest.java` | JUnit 6 tests |
| `animation/index.html` | Animated walkthrough with spoken narration |

Run the tests with `../gradlew :v1:test`.
