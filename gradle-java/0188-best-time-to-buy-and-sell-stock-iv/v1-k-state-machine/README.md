# 188. Best Time to Buy and Sell Stock IV — v1: k-state machine

**Difficulty:** Hard &nbsp;|&nbsp; **Topic:** Multidimensional DP &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/)

## Problem

You may complete **at most `k`** transactions (buy then sell, never holding two shares). Return the maximum profit.

**Example**
```
k = 2, prices = [2,4,1]         → 2
k = 2, prices = [3,2,6,5,0,3]   → 7
```

**Constraints**
* `1 <= k <= 100`; `1 <= prices.length <= 1000`

## Approach: k-state machine

> Generalize the two-trade state machine to k trades: buy[t] and sell[t] for t = 1..k.

**Arrays of states.** For each price and each `t = 1..k`: `buy[t] = max(buy[t], sell[t-1] - p)` and `sell[t] = max(sell[t], buy[t] + p)`.
If `k >= n/2`, the limit never binds, so simply add every positive daily rise (as in Stock II).

* Time: **O(n·k)** — k state updates per day.
* Space: **O(k)** — two arrays of size k + 1.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0188/v1/BestTimeToBuyAndSellStockIV.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0188/v1/BestTimeToBuyAndSellStockIVTest.java` | JUnit 6 tests |
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
