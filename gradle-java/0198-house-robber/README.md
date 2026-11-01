# 198. House Robber

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** 1D DP &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/house-robber/)

## Problem

Houses along a street hold `nums[i]` money. You cannot rob two **adjacent** houses. Return the maximum amount you can rob.

**Example**
```
[1,2,3,1] → 4 (1 + 3),   [2,7,9,3,1] → 12 (2 + 9 + 1)
```

**Constraints**
* `1 <= nums.length <= 100`; `0 <= nums[i] <= 400`

## Solutions

Each folder below is a separate, self-contained Gradle project, ordered from the simplest idea to the most efficient one.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-dp-table](v1-dp-table/README.md) | DP table | `O(n)` | `O(n)` | [▶ animation](v1-dp-table/animation/index.html) |
| [v2-two-rolling-variables](v2-two-rolling-variables/README.md) | Two rolling variables | `O(n)` | `O(1)` | [▶ animation](v2-two-rolling-variables/animation/index.html) |
