# 283. Move Zeroes

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Two Pointers &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/move-zeroes/)

## Problem

Move all `0`s in `nums` to the end **in place**, keeping the relative order of the non-zero values.

**Example**
```
[0,1,0,3,12] → [1,3,12,0,0]
```

**Constraints**
* `1 <= nums.length <= 10^4`

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-swap-with-write-pointer](v1-swap-with-write-pointer/README.md) | Swap with write pointer | `O(n)` | `O(1)` | [▶ animation](v1-swap-with-write-pointer/animation/index.html) |
