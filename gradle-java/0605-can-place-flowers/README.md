# 605. Can Place Flowers

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Greedy &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/can-place-flowers/)

## Problem

A flowerbed is an array of `0` (empty) and `1` (planted); flowers may not be adjacent. Return `true` if `n` new flowers can be planted.

**Example**
```
flowerbed = [1,0,0,0,1], n = 1 → true
flowerbed = [1,0,0,0,1], n = 2 → false
```

**Constraints**
* `1 <= flowerbed.length <= 2 * 10^4`

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-greedy-left-to-right](v1-greedy-left-to-right/README.md) | Greedy left to right | `O(n)` | `O(1)` | [▶ animation](v1-greedy-left-to-right/animation/index.html) |
