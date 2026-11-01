# 1. Two Sum

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Hashmap &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/two-sum/)

## Problem

Given an integer array `nums` and an integer `target`, return the indices of the two numbers that add up to `target`.
Exactly one solution exists, and you may not use the same element twice. Return the indices in any order.

**Example 1**
```
Input:  nums = [2,7,11,15], target = 9
Output: [0,1]
```

**Example 2**
```
Input:  nums = [3,2,4], target = 6
Output: [1,2]
```

**Example 3**
```
Input:  nums = [3,3], target = 6
Output: [0,1]
```

**Constraints**
* `2 <= nums.length <= 10^4`; `-10^9 <= nums[i], target <= 10^9`

**Follow-up:** better than O(n²)?

## Solutions

Each folder below is a separate, self-contained Gradle project, ordered from the simplest idea to the most efficient one.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-brute-force](v1-brute-force/README.md) | Brute force | `O(n²)` | `O(1)` | [▶ animation](v1-brute-force/animation/index.html) |
| [v2-one-pass-hash-map](v2-one-pass-hash-map/README.md) | One-pass hash map | `O(n)` | `O(n)` | [▶ animation](v2-one-pass-hash-map/animation/index.html) |
