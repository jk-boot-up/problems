# 31. Next Permutation

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Two Pointers &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/next-permutation/)

## Problem

Rearrange `nums` **in place** into the next lexicographically greater permutation. If it is the largest permutation, rearrange it
into the smallest (ascending) one.

**Example**
```
[1,2,3] → [1,3,2],   [3,2,1] → [1,2,3],   [1,1,5] → [1,5,1]
```

**Constraints**
* `1 <= nums.length <= 100`

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-pivot-swap-reverse](v1-pivot-swap-reverse/README.md) | Pivot, swap, reverse | `O(n)` | `O(1)` | [▶ animation](v1-pivot-swap-reverse/animation/index.html) |
