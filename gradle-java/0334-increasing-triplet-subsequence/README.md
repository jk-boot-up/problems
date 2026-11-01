# 334. Increasing Triplet Subsequence

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Greedy &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/increasing-triplet-subsequence/)

## Problem

Return `true` if there are indices `i < j < k` with `nums[i] < nums[j] < nums[k]`.

**Example**
```
[1,2,3,4,5] → true,   [5,4,3,2,1] → false,   [2,1,5,0,4,6] → true
```

**Constraints**
* `1 <= nums.length <= 5 * 10^5`

**Follow-up:** O(n) time, O(1) space.

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-two-smallest-tails](v1-two-smallest-tails/README.md) | Two smallest tails | `O(n)` | `O(1)` | [▶ animation](v1-two-smallest-tails/animation/index.html) |
