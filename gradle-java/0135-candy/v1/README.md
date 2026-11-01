# 135. Candy — v1: Optimal

[← Problem statement](../README.md)

> Satisfy left neighbours in one pass and right neighbours in a second pass, taking the max at each child.

## Approach

**Two passes.** Start everyone at 1. Left to right: if `ratings[i] > ratings[i-1]`, set `candy[i] = candy[i-1] + 1`.
Right to left: if `ratings[i] > ratings[i+1]`, set `candy[i] = max(candy[i], candy[i+1] + 1)`. Both rules now hold with the
fewest candies.

* Time: **O(n)** — two passes.
* Space: **O(n)** — the candy array.

## Files

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0135/v1/Candy.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0135/v1/CandyTest.java` | JUnit 6 tests |
| `animation/index.html` | Animated walkthrough with spoken narration |

Run the tests with `../gradlew :v1:test`.
