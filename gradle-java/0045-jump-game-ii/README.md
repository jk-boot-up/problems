# 45. Jump Game II

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Array / String &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/jump-game-ii/)

## Problem

You start at index `0` of `nums`; `nums[i]` is the maximum jump length from `i`. The last index is always reachable.
Return the **minimum number of jumps** needed to reach the last index.

**Example 1**
```
Input:  nums = [2,3,1,1,4]
Output: 2   (0 → 1 → 4)
```

**Example 2**
```
Input:  nums = [2,3,0,1,4]
Output: 2
```

**Constraints**
* `1 <= nums.length <= 10^4`
* `0 <= nums[i] <= 1000`
* The last index is reachable.

## Solutions

Each folder below is a separate, self-contained Gradle project, ordered from the simplest idea to the most efficient one.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-dynamic-programming](v1-dynamic-programming/README.md) | Dynamic programming | `O(n²)` | `O(n)` | [▶ animation](v1-dynamic-programming/animation/index.html) |
| [v2-greedy-windows](v2-greedy-windows/README.md) | Greedy windows | `O(n)` | `O(1)` | [▶ animation](v2-greedy-windows/animation/index.html) |
