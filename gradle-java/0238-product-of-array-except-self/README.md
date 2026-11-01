# 238. Product of Array Except Self

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Array / String &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/product-of-array-except-self/)

## Problem

Given an integer array `nums`, return an array `answer` where `answer[i]` equals the product of every element of `nums`
**except** `nums[i]`. Do it in O(n) time **without using division**. Every prefix/suffix product fits in a 32-bit integer.

**Example 1**
```
Input:  nums = [1,2,3,4]
Output: [24,12,8,6]
```

**Example 2**
```
Input:  nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
```

**Constraints**
* `2 <= nums.length <= 10^5`
* `-30 <= nums[i] <= 30`

**Follow-up:** O(1) extra space (the output array does not count).

## Solutions

Each folder below is a separate, self-contained Gradle project, ordered from the simplest idea to the most efficient one.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-prefix-and-suffix-arrays](v1-prefix-and-suffix-arrays/README.md) | Prefix and suffix arrays | `O(n)` | `O(n)` | [▶ animation](v1-prefix-and-suffix-arrays/animation/index.html) |
| [v2-output-array-running-suffix](v2-output-array-running-suffix/README.md) | Output array + running suffix | `O(n)` | `O(1)` | [▶ animation](v2-output-array-running-suffix/animation/index.html) |
