# 123. Best Time to Buy and Sell Stock III

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

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-four-state-machine](v1-four-state-machine/README.md) | Four-state machine | `O(n)` | `O(1)` | [▶ animation](v1-four-state-machine/animation/index.html) |
