# 309. Best Time to Buy and Sell Stock with Cooldown

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

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-three-state-machine](v1-three-state-machine/README.md) | Three-state machine | `O(n)` | `O(1)` | [▶ animation](v1-three-state-machine/animation/index.html) |
