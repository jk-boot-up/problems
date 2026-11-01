# 322. Coin Change

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** 1D DP &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/coin-change/)

## Problem

Given coin denominations `coins` (unlimited supply of each) and an `amount`, return the fewest coins that add up to `amount`, or `-1`
if it is impossible.

**Example**
```
coins = [1,2,5], amount = 11 → 3 (5 + 5 + 1)
coins = [2],     amount = 3  → -1
coins = [1],     amount = 0  → 0
```

**Constraints**
* `1 <= coins.length <= 12`; `1 <= coins[i] <= 2^31 - 1`; `0 <= amount <= 10^4`

## Solutions

Each folder below is a separate, self-contained Gradle project, ordered from the simplest idea to the most efficient one.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-top-down-memoized-recursion](v1-top-down-memoized-recursion/README.md) | Top-down memoized recursion | `O(amount · coins)` | `O(amount)` | [▶ animation](v1-top-down-memoized-recursion/animation/index.html) |
| [v2-bottom-up-dp](v2-bottom-up-dp/README.md) | Bottom-up DP | `O(amount · coins)` | `O(amount)` | [▶ animation](v2-bottom-up-dp/animation/index.html) |
