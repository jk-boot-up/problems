# 128. Longest Consecutive Sequence

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Hashmap &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/longest-consecutive-sequence/)

## Problem

Given an unsorted integer array `nums`, return the length of the longest run of consecutive integers (e.g. 1, 2, 3, 4) that can be
formed from its values. Your algorithm must run in **O(n)** time.

**Example 1**
```
Input:  nums = [100,4,200,1,3,2]
Output: 4   (1, 2, 3, 4)
```

**Example 2**
```
Input:  nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
```

**Constraints**
* `0 <= nums.length <= 10^5`; `-10^9 <= nums[i] <= 10^9`

## Solutions

Each folder below is a separate, self-contained Gradle project, ordered from the simplest idea to the most efficient one.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-sort-and-scan](v1-sort-and-scan/README.md) | Sort and scan | `O(n log n)` | `O(log n)` | [▶ animation](v1-sort-and-scan/animation/index.html) |
| [v2-hash-set-count-from-run-starts](v2-hash-set-count-from-run-starts/README.md) | Hash set, count from run starts | `O(n)` | `O(n)` | [▶ animation](v2-hash-set-count-from-run-starts/animation/index.html) |
