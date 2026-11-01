# 1512. Number of Good Pairs

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Arrays & Hashing &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/number-of-good-pairs/)

## Problem

A pair `(i, j)` is good if `nums[i] == nums[j]` and `i < j`. Return the number of good pairs.

**Example**
```
[1,2,3,1,1,3] → 4,   [1,1,1,1] → 6,   [1,2,3] → 0
```

**Constraints**
* `1 <= nums.length <= 100`; `1 <= nums[i] <= 100`

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-running-counts](v1-running-counts/README.md) | Running counts | `O(n)` | `O(1)` | [▶ animation](v1-running-counts/animation/index.html) |
