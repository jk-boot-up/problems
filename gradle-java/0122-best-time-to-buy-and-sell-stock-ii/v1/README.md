# 122. Best Time to Buy and Sell Stock II — v1: Optimal

[← Problem statement](../README.md)

> With unlimited trades, collect every positive day-to-day rise.

## Approach

**Greedy.** Any profitable run from a valley to a peak equals the sum of its daily increases. So add
`prices[i] - prices[i-1]` whenever it is positive.

* Time: **O(n)** — one comparison per neighbouring pair of days.
* Space: **O(1)** — a running total.

## Files

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0122/v1/BestTimeToBuyAndSellStockII.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0122/v1/BestTimeToBuyAndSellStockIITest.java` | JUnit 6 tests |
| `animation/index.html` | Animated walkthrough with spoken narration |

Run the tests with `../gradlew :v1:test`.
