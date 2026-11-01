# 41. First Missing Positive

**Difficulty:** Hard &nbsp;|&nbsp; **Topic:** Arrays & Hashing &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/first-missing-positive/)

## Problem

Return the smallest **positive** integer that does not appear in the unsorted array `nums`, in O(n) time and O(1) extra space.

**Example**
```
[1,2,0] → 3,   [3,4,-1,1] → 2,   [7,8,9,11,12] → 1
```

**Constraints**
* `1 <= nums.length <= 10^5`

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-cyclic-placement](v1-cyclic-placement/README.md) | Cyclic placement | `O(n)` | `O(1)` | [▶ animation](v1-cyclic-placement/animation/index.html) |
