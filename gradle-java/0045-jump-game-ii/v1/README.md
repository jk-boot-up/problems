# 45. Jump Game II — v1: Dynamic programming

[← Problem statement](../README.md)

> jumps[i] = fewest jumps to reach i; relax every index reachable from i.

## Approach

**DP over positions.** `dp[0] = 0`, every other entry starts at infinity. For each `i`, for each `j` in `i+1 … i+nums[i]`,
set `dp[j] = min(dp[j], dp[i] + 1)`.

* Time: **O(n²)** — each index may relax up to n later indices.
* Space: **O(n)** — the dp array.

## Files

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0045/v1/JumpGameII.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0045/v1/JumpGameIITest.java` | JUnit 6 tests |
| `animation/index.html` | Animated walkthrough with spoken narration |

Run the tests with `../gradlew :v1:test`.
