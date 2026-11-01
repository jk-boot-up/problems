# 27. Remove Element

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Array / String &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/remove-element/)

## Problem

Given an integer array `nums` and an integer `val`, remove every occurrence of `val` **in place** and return `k`, the number
of elements that are not equal to `val`. The first `k` slots of `nums` must hold those elements (in any order); what remains after
index `k - 1` does not matter.

**Example 1**
```
Input:  nums = [3,2,2,3], val = 3
Output: 2, nums = [2,2,_,_]
```

**Example 2**
```
Input:  nums = [0,1,2,2,3,0,4,2], val = 2
Output: 5, nums = [0,1,3,0,4,_,_,_]
```

**Constraints**
* `0 <= nums.length <= 100`
* `0 <= nums[i] <= 50`, `0 <= val <= 100`

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-read-write-pointers](v1-read-write-pointers/README.md) | Read-write pointers | `O(n)` | `O(1)` | [▶ animation](v1-read-write-pointers/animation/index.html) |
