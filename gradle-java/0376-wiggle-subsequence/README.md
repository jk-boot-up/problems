# 376. Wiggle Subsequence

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Greedy &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/wiggle-subsequence/)

## Problem

A **wiggle sequence** has differences that strictly alternate between positive and negative (a single element, or two different
elements, also count). Return the length of the longest wiggle **subsequence** of `nums`.

**Example**
```
[1,7,4,9,2,5]               → 6
[1,17,5,10,13,15,10,5,16,8] → 7
[1,2,3,4,5,6,7,8,9]         → 2
```

**Constraints**
* `1 <= nums.length <= 1000`

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-up-down-greedy](v1-up-down-greedy/README.md) | Up/down greedy | `O(n)` | `O(1)` | [▶ animation](v1-up-down-greedy/animation/index.html) |
