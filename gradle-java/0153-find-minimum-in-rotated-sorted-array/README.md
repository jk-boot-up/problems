# 153. Find Minimum in Rotated Sorted Array

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Binary Search &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/)

## Problem

A sorted array of **unique** values was rotated between 1 and n times. Return its minimum element in O(log n).

**Example**
```
[3,4,5,1,2] → 1,  [4,5,6,7,0,1,2] → 0,  [11,13,15,17] → 11
```

**Constraints**
* `1 <= n <= 5000`; values are unique.

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-binary-search-against-the-right-end](v1-binary-search-against-the-right-end/README.md) | Binary search against the right end | `O(log n)` | `O(1)` | [▶ animation](v1-binary-search-against-the-right-end/animation/index.html) |
