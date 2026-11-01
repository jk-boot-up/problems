# 1493. Longest Subarray of 1's After Deleting One Element

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Sliding Window &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/)

## Problem

Delete exactly one element from a binary array. Return the length of the longest non-empty subarray of only `1`s in the result (0 if none).

**Example**
```
[1,1,0,1] → 3,   [0,1,1,1,0,1,1,0,1] → 5,   [1,1,1] → 2
```

**Constraints**
* `1 <= nums.length <= 10^5`

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-sliding-window-with-one-zero](v1-sliding-window-with-one-zero/README.md) | Sliding window with one zero | `O(n)` | `O(1)` | [▶ animation](v1-sliding-window-with-one-zero/animation/index.html) |
