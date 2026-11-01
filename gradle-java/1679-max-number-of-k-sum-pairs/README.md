# 1679. Max Number of K-Sum Pairs

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Arrays & Hashing &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/max-number-of-k-sum-pairs/)

## Problem

In one operation, remove two numbers whose sum is `k`. Return the maximum number of operations.

**Example**
```
nums = [1,2,3,4], k = 5   → 2
nums = [3,1,3,4,3], k = 6 → 1
```

**Constraints**
* `1 <= nums.length <= 10^5`

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-hash-map-of-waiting-numbers](v1-hash-map-of-waiting-numbers/README.md) | Hash map of waiting numbers | `O(n)` | `O(n)` | [▶ animation](v1-hash-map-of-waiting-numbers/animation/index.html) |
