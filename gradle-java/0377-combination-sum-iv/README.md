# 377. Combination Sum IV

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Dynamic Programming &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/combination-sum-iv/)

## Problem

Given distinct positive integers `nums` and a `target`, return the number of **ordered** sequences of numbers from `nums` (repeats allowed)
that add up to `target`. The answer fits in a 32-bit integer.

**Example**
```
nums = [1,2,3], target = 4 → 7
   (1,1,1,1) (1,1,2) (1,2,1) (1,3) (2,1,1) (2,2) (3,1)
nums = [9], target = 3 → 0
```

**Constraints**
* `1 <= nums.length <= 200`, `1 <= nums[i], target <= 1000`

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-dp-over-the-target](v1-dp-over-the-target/README.md) | DP over the target | `O(target · n)` | `O(target)` | [▶ animation](v1-dp-over-the-target/animation/index.html) |
