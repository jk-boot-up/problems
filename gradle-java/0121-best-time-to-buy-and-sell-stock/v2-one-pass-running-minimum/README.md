# 121. Best Time to Buy and Sell Stock — v2: One pass, running minimum

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Array / String &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)

## Problem

`prices[i]` is a stock's price on day `i`. Pick **one** day to buy and a **later** day to sell to maximize profit.
Return the maximum profit, or `0` if no profitable trade exists.

**Example 1**
```
Input:  prices = [7,1,5,3,6,4]
Output: 5   (buy at 1 on day 1, sell at 6 on day 4)
```

**Example 2**
```
Input:  prices = [7,6,4,3,1]
Output: 0
```

**Constraints**
* `1 <= prices.length <= 10^5`
* `0 <= prices[i] <= 10^4`

## Approach: One pass, running minimum

> Track the lowest price so far; selling today earns today's price minus that minimum.

**One pass with a running minimum.** For each day, the best sale today uses the cheapest price seen before it.
Keep `minPrice` and `best = max(best, price - minPrice)`.

* Time: **O(n)** — each day is visited once.
* Space: **O(1)** — two numbers: the minimum so far and the best profit.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0121/v2/BestTimeToBuyAndSellStock.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0121/v2/BestTimeToBuyAndSellStockTest.java` | JUnit 6 tests |
| `animation/index.html` | Animated walkthrough with spoken narration |

## Build and test

This folder is a standalone Gradle 9.8.2 project. Only a JDK is needed to start Gradle; JDK 25 is downloaded
automatically if it is missing.

```bash
./gradlew test
```

## Animation

Open [`animation/index.html`](animation/index.html) in a browser. It has three tabs:

* **Problem:** the statement and the key idea.
* **Walkthrough:** pick a scenario and press **Play**. Each step is animated and read aloud by your browser's speech
  engine (use the 🔊 *Narration* button to turn the voice on or off; a female voice, Amy when installed, is preferred). Keys: space = play/pause, ← / → = step, 1–9 = scenario.
* **Complexity:** time and space cost, plotted against the common growth curves, and compared with the other approaches.

Switch between Light, Medium and Dark themes in the header.

## Other approaches

* [v1-brute-force](../v1-brute-force/README.md): Brute force (`O(n²)` time, `O(1)` space)
