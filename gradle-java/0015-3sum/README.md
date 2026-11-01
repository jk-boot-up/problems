# 15. 3Sum

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Two Pointers &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/3sum/)

## Problem

Return all **unique** triplets `[a, b, c]` from `nums` (at different indices) with `a + b + c == 0`. The answer must not
contain duplicate triplets; order does not matter.

**Example 1**
```
Input:  nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
```

**Example 2**
```
Input:  nums = [0,1,1]
Output: []
```

**Example 3**
```
Input:  nums = [0,0,0]
Output: [[0,0,0]]
```

**Constraints**
* `3 <= nums.length <= 3000`
* `-10^5 <= nums[i] <= 10^5`

## Solutions

Each folder below is a separate, self-contained Gradle project, ordered from the simplest idea to the most efficient one.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-hash-set-per-fixed-number](v1-hash-set-per-fixed-number/README.md) | Hash set per fixed number | `O(n²)` | `O(n)` | [▶ animation](v1-hash-set-per-fixed-number/animation/index.html) |
| [v2-sort-two-pointers](v2-sort-two-pointers/README.md) | Sort + two pointers | `O(n²)` | `O(1)` | [▶ animation](v2-sort-two-pointers/animation/index.html) |
