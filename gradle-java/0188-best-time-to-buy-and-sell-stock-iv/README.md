# 188. Best Time to Buy and Sell Stock IV

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

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-k-state-machine](v1-k-state-machine/README.md) | k-state machine | `O(n·k)` | `O(k)` | [▶ animation](v1-k-state-machine/animation/index.html) |
