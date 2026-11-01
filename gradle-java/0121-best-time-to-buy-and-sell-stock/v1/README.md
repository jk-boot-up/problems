# 121. Best Time to Buy and Sell Stock — v1: Brute force

[← Problem statement](../README.md)

> Try every buy day with every later sell day and keep the best difference.

## Approach

**All pairs.** For every `i < j`, compute `prices[j] - prices[i]` and keep the maximum.

* Time: **O(n²)** — about n²/2 pairs.
* Space: **O(1)** — a running best.

## Files

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0121/v1/BestTimeToBuyAndSellStock.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0121/v1/BestTimeToBuyAndSellStockTest.java` | JUnit 6 tests |
| `animation/index.html` | Animated walkthrough with spoken narration |

Run the tests with `../gradlew :v1:test`.
