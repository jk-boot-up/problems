# 1438. Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Sliding Window &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/)

## Problem

Return the length of the longest non-empty subarray in which the absolute difference between **any** two elements is at most `limit`
(equivalently, `max - min <= limit`).

**Example**
```
nums = [8,2,4,7],         limit = 4 → 2   ([2,4] or [4,7])
nums = [10,1,2,4,7,2],    limit = 5 → 4   ([2,4,7,2])
nums = [4,2,2,2,4,4,2,2], limit = 0 → 3
```

**Constraints**
* `1 <= nums.length <= 10^5`

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-window-with-max-min-deques](v1-window-with-max-min-deques/README.md) | Window with max/min deques | `O(n)` | `O(n)` | [▶ animation](v1-window-with-max-min-deques/animation/index.html) |
