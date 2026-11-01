# 121. Best Time to Buy and Sell Stock — v2: One pass, running minimum

[← Problem statement](../README.md)

> Track the lowest price so far; selling today earns today's price minus that minimum.

## Approach

**One pass with a running minimum.** For each day, the best sale today uses the cheapest price seen before it.
Keep `minPrice` and `best = max(best, price - minPrice)`.

* Time: **O(n)** — each day is visited once.
* Space: **O(1)** — two numbers: the minimum so far and the best profit.

## Files

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0121/v2/BestTimeToBuyAndSellStock.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0121/v2/BestTimeToBuyAndSellStockTest.java` | JUnit 6 tests |
| `animation/index.html` | Animated walkthrough with spoken narration |

Run the tests with `../gradlew :v2:test`.
