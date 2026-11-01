# 162. Find Peak Element

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Binary Search &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/find-peak-element/)

## Problem

A **peak** is an element strictly greater than its neighbours. Given `nums` (with `nums[-1] = nums[n] = -∞` and no two adjacent values
equal), return the index of **any** peak, in O(log n).

**Example**
```
Input:  nums = [1,2,1,3,5,6,4]
Output: 1 or 5
```

**Constraints**
* `1 <= nums.length <= 1000`; `nums[i] != nums[i + 1]`

## Solutions

Each folder below is a separate, self-contained Gradle project, ordered from the simplest idea to the most efficient one.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-linear-scan](v1-linear-scan/README.md) | Linear scan | `O(n)` | `O(1)` | [▶ animation](v1-linear-scan/animation/index.html) |
| [v2-binary-search-uphill](v2-binary-search-uphill/README.md) | Binary search uphill | `O(log n)` | `O(1)` | [▶ animation](v2-binary-search-uphill/animation/index.html) |
