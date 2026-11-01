# 169. Majority Element

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Array / String &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/majority-element/)

## Problem

Given an array `nums` of size `n`, return the **majority element**: the value that appears more than `⌊n / 2⌋` times.
You may assume a majority element always exists.

**Example 1**
```
Input:  nums = [3,2,3]
Output: 3
```

**Example 2**
```
Input:  nums = [2,2,1,1,1,2,2]
Output: 2
```

**Constraints**
* `1 <= n <= 5 * 10^4`
* `-10^9 <= nums[i] <= 10^9`

**Follow-up:** solve it in linear time and O(1) space.

## Solutions

Each folder below is a separate, self-contained Gradle project, ordered from the simplest idea to the most efficient one.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-hash-map-counting](v1-hash-map-counting/README.md) | Hash map counting | `O(n)` | `O(n)` | [▶ animation](v1-hash-map-counting/animation/index.html) |
| [v2-sort-and-take-the-middle](v2-sort-and-take-the-middle/README.md) | Sort and take the middle | `O(n log n)` | `O(log n)` | [▶ animation](v2-sort-and-take-the-middle/animation/index.html) |
| [v3-boyer-moore-voting](v3-boyer-moore-voting/README.md) | Boyer–Moore voting | `O(n)` | `O(1)` | [▶ animation](v3-boyer-moore-voting/animation/index.html) |
