# 1539. Kth Missing Positive Number

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Binary Search &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/kth-missing-positive-number/)

## Problem

Given a strictly increasing array of positive integers and `k`, return the `k`-th positive integer missing from the array.

**Example**
```
arr = [2,3,4,7,11], k = 5 → 9    (missing: 1,5,6,8,9,…)
arr = [1,2,3,4],    k = 2 → 6
```

**Constraints**
* `1 <= arr.length <= 1000`, `1 <= arr[i], k <= 1000`

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-binary-search-on-missing-counts](v1-binary-search-on-missing-counts/README.md) | Binary search on missing counts | `O(log n)` | `O(1)` | [▶ animation](v1-binary-search-on-missing-counts/animation/index.html) |
