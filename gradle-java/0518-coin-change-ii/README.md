# 518. Coin Change II

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** 1D DP &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/coin-change-ii/)

## Problem

Return the number of **combinations** of coins (unlimited supply) that make up `amount`. Order does not matter.

**Example**
```
amount = 5, coins = [1,2,5] → 4,   amount = 3, coins = [2] → 0,   amount = 10, coins = [10] → 1
```

**Constraints**
* `0 <= amount <= 5000`; `1 <= coins.length <= 300`

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-unbounded-knapsack-counting](v1-unbounded-knapsack-counting/README.md) | Unbounded knapsack counting | `O(coins · amount)` | `O(amount)` | [▶ animation](v1-unbounded-knapsack-counting/animation/index.html) |
