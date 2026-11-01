# 350. Intersection of Two Arrays II

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Arrays & Hashing &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/intersection-of-two-arrays-ii/)

## Problem

Return the intersection of `nums1` and `nums2`, where each value appears as many times as it shows in **both** arrays, in any order.

**Example**
```
[1,2,2,1], [2,2] → [2,2],   [4,9,5], [9,4,9,8,4] → [4,9]
```

**Constraints**
* `1 <= length <= 1000`

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-hash-map-counts](v1-hash-map-counts/README.md) | Hash map counts | `O(m + n)` | `O(m)` | [▶ animation](v1-hash-map-counts/animation/index.html) |
