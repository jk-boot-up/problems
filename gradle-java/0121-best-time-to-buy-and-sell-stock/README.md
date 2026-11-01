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

Each folder below is a separate, self-contained Gradle project, ordered from the simplest idea to the most efficient one.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-brute-force](v1-brute-force/README.md) | Brute force | `O(n²)` | `O(1)` | [▶ animation](v1-brute-force/animation/index.html) |
| [v2-one-pass-running-minimum](v2-one-pass-running-minimum/README.md) | One pass, running minimum | `O(n)` | `O(1)` | [▶ animation](v2-one-pass-running-minimum/animation/index.html) |
