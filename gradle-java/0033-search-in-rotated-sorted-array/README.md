# 33. Search in Rotated Sorted Array

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Binary Search &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/search-in-rotated-sorted-array/)

## Problem

A sorted array of **distinct** integers was rotated at an unknown pivot (e.g. `[0,1,2,4,5,6,7]` → `[4,5,6,7,0,1,2]`). Return the index
of `target`, or `-1`, in O(log n).

**Example**
```
nums = [4,5,6,7,0,1,2]:  target 0 → 4,  target 3 → -1
```

**Constraints**
* `1 <= nums.length <= 5000`; values are distinct.

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-binary-search-on-the-sorted-half](v1-binary-search-on-the-sorted-half/README.md) | Binary search on the sorted half | `O(log n)` | `O(1)` | [▶ animation](v1-binary-search-on-the-sorted-half/animation/index.html) |
