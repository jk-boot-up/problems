# 154. Find Minimum in Rotated Sorted Array II

**Difficulty:** Hard &nbsp;|&nbsp; **Topic:** Binary Search &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/)

## Problem

A sorted array that may contain **duplicates** was rotated. Return its minimum value.

**Example**
```
[1,3,5] → 1,   [2,2,2,0,1] → 0,   [3,1,3] → 1
```

**Constraints**
* `1 <= n <= 5000`

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-binary-search-with-duplicate-shrinking](v1-binary-search-with-duplicate-shrinking/README.md) | Binary search with duplicate shrinking | `O(n)` | `O(1)` | [▶ animation](v1-binary-search-with-duplicate-shrinking/animation/index.html) |
