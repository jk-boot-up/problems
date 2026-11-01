# 1283. Find the Smallest Divisor Given a Threshold

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Binary Search &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/find-the-smallest-divisor-given-a-threshold/)

## Problem

Choose a positive integer divisor, divide every element of `nums` by it rounding **up**, and add the results. Return the smallest divisor
for which this sum is at most `threshold`.

**Example**
```
nums = [1,2,5,9], threshold = 6 → 5   (1 + 1 + 1 + 2 = 5)
nums = [44,22,33,11,1], threshold = 5 → 44
```

**Constraints**
* `1 <= nums.length <= 5 * 10^4 <= threshold <= 10^6`, `1 <= nums[i] <= 10^6`

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-binary-search-on-the-divisor](v1-binary-search-on-the-divisor/README.md) | Binary search on the divisor | `O(n log M)` | `O(1)` | [▶ animation](v1-binary-search-on-the-divisor/animation/index.html) |
