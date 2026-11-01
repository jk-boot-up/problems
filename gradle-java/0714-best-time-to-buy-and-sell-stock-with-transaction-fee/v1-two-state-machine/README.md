# 714. Best Time to Buy and Sell Stock with Transaction Fee — v1: Two-state machine

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** 1D DP &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/)

## Problem

You may trade as many times as you like, holding at most one share, and every sale costs `fee`. Return the maximum profit.

**Example**
```
prices = [1,3,2,8,4,9], fee = 2 → 8   ((8 − 1 − 2) + (9 − 4 − 2))
```

**Constraints**
* `1 <= prices.length <= 5 * 10^4`

## Approach: Two-state machine

> Two states: holding or not; selling pays the fee.

**DP.** `cash = max(cash, hold + p - fee)` (sell today) and `hold = max(hold, cash - p)` (buy today).

* Time: **O(n)** — one pass.
* Space: **O(1)** — two numbers.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0714/v1/StockWithFee.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0714/v1/StockWithFeeTest.java` | JUnit 6 tests |
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
