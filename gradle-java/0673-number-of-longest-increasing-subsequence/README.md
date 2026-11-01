# 673. Number of Longest Increasing Subsequence

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Dynamic Programming &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/number-of-longest-increasing-subsequence/)

## Problem

Return the number of **longest strictly increasing** subsequences of `nums`.

**Example**
```
[1,3,5,4,7] → 2   ([1,3,4,7] and [1,3,5,7])
[2,2,2,2,2] → 5   (each single element)
```

**Constraints**
* `1 <= nums.length <= 2000`

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-length-and-count-dp](v1-length-and-count-dp/README.md) | Length and count DP | `O(n²)` | `O(n)` | [▶ animation](v1-length-and-count-dp/animation/index.html) |
