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

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-greedy-daily-gains](v1-greedy-daily-gains/README.md) | Greedy daily gains | `O(n)` | `O(1)` | [▶ animation](v1-greedy-daily-gains/animation/index.html) |
