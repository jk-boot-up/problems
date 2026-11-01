# 1838. Frequency of the Most Frequent Element

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Sliding Window &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/frequency-of-the-most-frequent-element/)

## Problem

In one operation you may increase any element by 1. With at most `k` operations, return the largest possible frequency of a single value.

**Example**
```
nums = [1,2,4],    k = 5 → 3   (raise 1 and 2 to 4)
nums = [1,4,8,13], k = 5 → 2
nums = [3,9,6],    k = 2 → 1
```

**Constraints**
* `1 <= nums.length <= 10^5`, `1 <= nums[i] <= 10^5`, `1 <= k <= 10^5`

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-sort-sliding-window](v1-sort-sliding-window/README.md) | Sort + sliding window | `O(n log n)` | `O(1)` | [▶ animation](v1-sort-sliding-window/animation/index.html) |
