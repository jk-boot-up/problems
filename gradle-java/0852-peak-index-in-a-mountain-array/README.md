# 852. Peak Index in a Mountain Array

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Binary Search &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/peak-index-in-a-mountain-array/)

## Problem

`arr` strictly increases then strictly decreases. Return the index of the peak in O(log n).

**Example**
```
[0,1,0] → 1,   [0,2,1,0] → 1,   [0,10,5,2] → 1
```

**Constraints**
* `3 <= arr.length <= 10^5`

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-binary-search-on-the-slope](v1-binary-search-on-the-slope/README.md) | Binary search on the slope | `O(log n)` | `O(1)` | [▶ animation](v1-binary-search-on-the-slope/animation/index.html) |
