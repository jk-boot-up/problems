# 714. Best Time to Buy and Sell Stock with Transaction Fee

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** 1D DP &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/)

## Problem

You may trade as many times as you like, holding at most one share, and every sale costs `fee`. Return the maximum profit.

**Example**
```
prices = [1,3,2,8,4,9], fee = 2 → 8   ((8 − 1 − 2) + (9 − 4 − 2))
```

**Constraints**
* `1 <= prices.length <= 5 * 10^4`

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-two-state-machine](v1-two-state-machine/README.md) | Two-state machine | `O(n)` | `O(1)` | [▶ animation](v1-two-state-machine/animation/index.html) |
