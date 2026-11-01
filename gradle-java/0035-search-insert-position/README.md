# 35. Search Insert Position

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Binary Search &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/search-insert-position/)

## Problem

Given a sorted array of **distinct** integers and a `target`, return the index of `target` if present, otherwise the index where it
would be inserted to keep the order. Run in O(log n).

**Example**
```
nums = [1,3,5,6]:  target 5 → 2,  target 2 → 1,  target 7 → 4
```

**Constraints**
* `1 <= nums.length <= 10^4`; sorted and distinct.

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-lower-bound-binary-search](v1-lower-bound-binary-search/README.md) | Lower-bound binary search | `O(log n)` | `O(1)` | [▶ animation](v1-lower-bound-binary-search/animation/index.html) |
