# 496. Next Greater Element I

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Stack &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/next-greater-element-i/)

## Problem

`nums1` is a subset of `nums2` (all values distinct). For each `x` in `nums1`, find the first value to the right of `x` in `nums2` that is
greater than `x`, or `-1`.

**Example**
```
nums1 = [4,1,2], nums2 = [1,3,4,2] → [-1,3,-1]
nums1 = [2,4],   nums2 = [1,2,3,4] → [3,-1]
```

**Constraints**
* `1 <= nums1.length <= nums2.length <= 1000`

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-monotonic-stack-hash-map](v1-monotonic-stack-hash-map/README.md) | Monotonic stack + hash map | `O(m + n)` | `O(n)` | [▶ animation](v1-monotonic-stack-hash-map/animation/index.html) |
