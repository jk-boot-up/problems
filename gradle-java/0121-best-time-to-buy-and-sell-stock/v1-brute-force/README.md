# 121. Best Time to Buy and Sell Stock — v1: Brute force

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

## Approach: Brute force

> Try every buy day with every later sell day and keep the best difference.

**All pairs.** For every `i < j`, compute `prices[j] - prices[i]` and keep the maximum.

* Time: **O(n²)** — about n²/2 pairs.
* Space: **O(1)** — a running best.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0121/v1/BestTimeToBuyAndSellStock.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0121/v1/BestTimeToBuyAndSellStockTest.java` | JUnit 6 tests |
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
  engine (untick *Narration* to mute). Keys: space = play/pause, ← / → = step, 1–9 = scenario.
* **Complexity:** time and space cost, plotted against the common growth curves, and compared with the other approaches.

Switch between Light, Medium and Dark themes in the header.

## Other approaches

* [v2-one-pass-running-minimum](../v2-one-pass-running-minimum/README.md): One pass, running minimum (`O(n)` time, `O(1)` space)
