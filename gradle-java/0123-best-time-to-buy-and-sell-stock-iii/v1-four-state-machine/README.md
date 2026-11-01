# 123. Best Time to Buy and Sell Stock III — v1: Four-state machine

**Difficulty:** Hard &nbsp;|&nbsp; **Topic:** Multidimensional DP &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/)

## Problem

`prices[i]` is the stock price on day `i`. You may complete **at most two** transactions (buy then sell), and must sell before buying
again. Return the maximum profit.

**Example**
```
[3,3,5,0,0,3,1,4] → 6   (buy 0 sell 3, buy 1 sell 4)
[1,2,3,4,5]       → 4
[7,6,4,3,1]       → 0
```

**Constraints**
* `1 <= prices.length <= 10^5`; `0 <= prices[i] <= 10^5`

## Approach: Four-state machine

> Track four running best balances: after the 1st buy, 1st sell, 2nd buy and 2nd sell.

**State machine.** `buy1` = best balance after the first buy (`max(buy1, -p)`), `sell1 = max(sell1, buy1 + p)`,
`buy2 = max(buy2, sell1 - p)`, `sell2 = max(sell2, buy2 + p)`. Each state builds on the one before it, on the same day, which is
harmless (it amounts to a zero-profit trade).

* Time: **O(n)** — one pass.
* Space: **O(1)** — four numbers.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0123/v1/BestTimeToBuyAndSellStockIII.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0123/v1/BestTimeToBuyAndSellStockIIITest.java` | JUnit 6 tests |
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
* **Complexity:** time and space cost, plotted against the common growth curves.

Switch between Light, Medium and Dark themes in the header.
