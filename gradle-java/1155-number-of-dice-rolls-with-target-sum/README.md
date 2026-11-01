# 1155. Number of Dice Rolls With Target Sum

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Dynamic Programming &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/number-of-dice-rolls-with-target-sum/)

## Problem

Roll `n` dice with `k` faces each (`1..k`). Return the number of ordered outcomes whose faces sum to `target`, modulo `10^9 + 7`.

**Example**
```
n = 1, k = 6, target = 3   → 1
n = 2, k = 6, target = 7   → 6
n = 30, k = 30, target = 500 → 222616187
```

**Constraints**
* `1 <= n, k <= 30`, `1 <= target <= 1000`

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-dp-over-dice-and-sums](v1-dp-over-dice-and-sums/README.md) | DP over dice and sums | `O(n · target · k)` | `O(target)` | [▶ animation](v1-dp-over-dice-and-sums/animation/index.html) |
