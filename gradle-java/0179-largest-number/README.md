# 179. Largest Number

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Sorting &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/largest-number/)

## Problem

Given non-negative integers `nums`, arrange them so they form the largest possible number, and return it as a string.

**Example**
```
[10,2]          → "210"
[3,30,34,5,9]   → "9534330"
[0,0]           → "0"
```

**Constraints**
* `1 <= nums.length <= 100`, `0 <= nums[i] <= 10^9`

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-sort-by-concatenation-order](v1-sort-by-concatenation-order/README.md) | Sort by concatenation order | `O(n log n · L)` | `O(n · L)` | [▶ animation](v1-sort-by-concatenation-order/animation/index.html) |
