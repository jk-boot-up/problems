# 724. Find Pivot Index

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Prefix Sum &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/find-pivot-index/)

## Problem

Return the leftmost index where the sum of the elements to its left equals the sum of the elements to its right (an empty side sums to 0),
or `-1`.

**Example**
```
[1,7,3,6,5,6] → 3,   [1,2,3] → -1,   [2,1,-1] → 0
```

**Constraints**
* `1 <= nums.length <= 10^4`

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-total-minus-running-left-sum](v1-total-minus-running-left-sum/README.md) | Total minus running left sum | `O(n)` | `O(1)` | [▶ animation](v1-total-minus-running-left-sum/animation/index.html) |
