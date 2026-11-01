# 525. Contiguous Array

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Prefix Sum &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/contiguous-array/)

## Problem

Given a binary array, return the length of the longest contiguous subarray with an equal number of 0s and 1s.

**Example**
```
[0,1]                 → 2
[0,1,0]               → 2
[0,1,1,1,1,1,0,0,0]   → 6
```

**Constraints**
* `1 <= nums.length <= 10^5`

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-earliest-index-of-each-balance](v1-earliest-index-of-each-balance/README.md) | Earliest index of each balance | `O(n)` | `O(n)` | [▶ animation](v1-earliest-index-of-each-balance/animation/index.html) |
