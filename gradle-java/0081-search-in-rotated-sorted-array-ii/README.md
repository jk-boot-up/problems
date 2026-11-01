# 81. Search in Rotated Sorted Array II

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Binary Search &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/search-in-rotated-sorted-array-ii/)

## Problem

A sorted array, possibly with **duplicates**, was rotated. Return `true` if `target` is in it.

**Example**
```
nums = [2,5,6,0,0,1,2]: target 0 → true, target 3 → false
```

**Constraints**
* `1 <= nums.length <= 5000`

**Follow-up:** duplicates can make the worst case linear — why?

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-binary-search-with-duplicate-skipping](v1-binary-search-with-duplicate-skipping/README.md) | Binary search with duplicate skipping | `O(n)` | `O(1)` | [▶ animation](v1-binary-search-with-duplicate-skipping/animation/index.html) |
