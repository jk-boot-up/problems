# 122. Best Time to Buy and Sell Stock II

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Array / String &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/)

## Problem

`prices[i]` is a stock's price on day `i`. You may buy and sell as many times as you like, but you can hold at most one share
at a time (you may sell and buy again on the same day). Return the maximum total profit.

**Example 1**
```
Input:  prices = [7,1,5,3,6,4]
Output: 7   (buy 1 → sell 5 = 4, buy 3 → sell 6 = 3)
```

**Example 2**
```
Input:  prices = [1,2,3,4,5]
Output: 4
```

**Example 3**
```
Input:  prices = [7,6,4,3,1]
Output: 0
```

**Constraints**
* `1 <= prices.length <= 3 * 10^4`
* `0 <= prices[i] <= 10^4`

## Solutions

One solution, in subproject `v1`.

| Version | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1](v1/README.md) | Optimal | `O(n)` | `O(1)` | [▶ animation](v1/animation/index.html) |

## Build and test

Only a JDK is needed to start Gradle; JDK 25 is downloaded automatically if it is missing.

```bash
./gradlew test          # every version
./gradlew :v1:test      # one version
```

## Animation

Open `vN/animation/index.html` in a browser. It has three tabs:

* **Problem:** the statement and the key idea.
* **Walkthrough:** pick a scenario and press **Play**. Each step is animated and read aloud by your browser's speech engine
  (untick *Narration* to mute). Keys: space = play/pause, ← / → = step, 1–9 = scenario.
* **Complexity:** time and space cost, plotted against the common growth curves, and compared across versions.

Use the header to switch between Light, Medium and Dark themes and between solution versions.
