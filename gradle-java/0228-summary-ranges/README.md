# 228. Summary Ranges

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Intervals &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/summary-ranges/)

## Problem

`nums` is sorted and has no duplicates. Return the smallest sorted list of ranges that covers every number exactly. A range
`[a,b]` is written `"a->b"` if `a != b`, else `"a"`.

**Example 1**
```
Input:  nums = [0,1,2,4,5,7]
Output: ["0->2","4->5","7"]
```

**Example 2**
```
Input:  nums = [0,2,3,4,6,8,9]
Output: ["0","2->4","6","8->9"]
```

**Constraints**
* `0 <= nums.length <= 20`; values fit in 32-bit integers; sorted, unique.

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-single-scan](v1-single-scan/README.md) | Single scan | `O(n)` | `O(1)` | [▶ animation](v1-single-scan/animation/index.html) |
