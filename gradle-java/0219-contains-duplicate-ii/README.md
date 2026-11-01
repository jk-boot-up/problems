# 219. Contains Duplicate II

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Hashmap &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/contains-duplicate-ii/)

## Problem

Return `true` if there are two **distinct** indices `i` and `j` with `nums[i] == nums[j]` and `|i - j| <= k`.

**Example 1**
```
Input:  nums = [1,2,3,1], k = 3
Output: true
```

**Example 2**
```
Input:  nums = [1,0,1,1], k = 1
Output: true
```

**Example 3**
```
Input:  nums = [1,2,3,1,2,3], k = 2
Output: false
```

**Constraints**
* `1 <= nums.length <= 10^5`; `0 <= k <= 10^5`

## Solutions

Each folder below is a separate, self-contained Gradle project, ordered from the simplest idea to the most efficient one.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-check-the-next-k-values](v1-check-the-next-k-values/README.md) | Check the next k values | `O(n·k)` | `O(1)` | [▶ animation](v1-check-the-next-k-values/animation/index.html) |
| [v2-last-index-map](v2-last-index-map/README.md) | Last-index map | `O(n)` | `O(n)` | [▶ animation](v2-last-index-map/animation/index.html) |
