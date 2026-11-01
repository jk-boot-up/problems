# 1658. Minimum Operations to Reduce X to Zero

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Sliding Window &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/)

## Problem

In one operation, remove the leftmost or rightmost element of `nums` and subtract it from `x`. Return the minimum number of operations to
make `x` exactly 0, or `-1`.

**Example**
```
nums = [1,1,4,2,3],    x = 5  → 2   (remove 3 and 2)
nums = [5,6,7,8,9],    x = 4  → -1
nums = [3,2,20,1,1,3], x = 10 → 5
```

**Constraints**
* `1 <= nums.length <= 10^5`, `1 <= nums[i] <= 10^4`, `1 <= x <= 10^9`

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-longest-middle-window](v1-longest-middle-window/README.md) | Longest middle window | `O(n)` | `O(1)` | [▶ animation](v1-longest-middle-window/animation/index.html) |
