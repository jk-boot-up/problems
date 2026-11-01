# 1004. Max Consecutive Ones III

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Sliding Window &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/max-consecutive-ones-iii/)

## Problem

Given a binary array and an integer `k`, return the longest run of `1`s you can get by flipping at most `k` zeros.

**Example**
```
nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2 → 6
nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3 → 10
```

**Constraints**
* `1 <= nums.length <= 10^5`; `0 <= k <= nums.length`

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-sliding-window-with-a-zero-budget](v1-sliding-window-with-a-zero-budget/README.md) | Sliding window with a zero budget | `O(n)` | `O(1)` | [▶ animation](v1-sliding-window-with-a-zero-budget/animation/index.html) |
