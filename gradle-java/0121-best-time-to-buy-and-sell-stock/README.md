# 121. Best Time to Buy and Sell Stock

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

## Solutions

Each version is a separate Gradle subproject, ordered from the simplest idea to the most efficient one.

| Version | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1](v1/README.md) | Brute force | `O(n²)` | `O(1)` | [▶ animation](v1/animation/index.html) |
| [v2](v2/README.md) | One pass, running minimum | `O(n)` | `O(1)` | [▶ animation](v2/animation/index.html) |

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
