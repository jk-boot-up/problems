# 309. Best Time to Buy and Sell Stock with Cooldown — v1: Three-state machine

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** 1D DP &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/)

## Problem

You may trade as many times as you like, holding at most one share, but after selling you must wait one day (cooldown) before buying
again. Return the maximum profit.

**Example**
```
[1,2,3,0,2] → 3   (buy, sell, cooldown, buy, sell)
[1]         → 0
```

**Constraints**
* `1 <= prices.length <= 5000`

## Approach: Three-state machine

> Three states per day: holding a share, just sold (cooling down), or resting free to buy.

**State machine.** `hold = max(hold, rest - p)` (buy only from rest), `sold = hold + p` (sell today), `rest = max(rest, prevSold)`
(yesterday's sale finishes its cooldown). Use the previous day's values for all three.

* Time: **O(n)** — one pass.
* Space: **O(1)** — three numbers.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0309/v1/StockWithCooldown.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0309/v1/StockWithCooldownTest.java` | JUnit 6 tests |
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
