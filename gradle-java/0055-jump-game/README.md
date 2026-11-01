# 55. Jump Game

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Array / String &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/jump-game/)

## Problem

You start at index `0` of `nums`. Each `nums[i]` is the **maximum** jump length from position `i`.
Return `true` if you can reach the last index, otherwise `false`.

**Example 1**
```
Input:  nums = [2,3,1,1,4]
Output: true   (0 → 1 → 4)
```

**Example 2**
```
Input:  nums = [3,2,1,0,4]
Output: false  (every path gets stuck at index 3)
```

**Constraints**
* `1 <= nums.length <= 10^4`
* `0 <= nums[i] <= 10^5`

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-greedy-reach](v1-greedy-reach/README.md) | Greedy reach | `O(n)` | `O(1)` | [▶ animation](v1-greedy-reach/animation/index.html) |
