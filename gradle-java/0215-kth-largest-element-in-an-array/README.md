# 215. Kth Largest Element in an Array

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Heap &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/kth-largest-element-in-an-array/)

## Problem

Return the `k`-th largest element of `nums` (in sorted order, not the k-th distinct value). Can you solve it without sorting?

**Example**
```
nums = [3,2,1,5,6,4], k = 2        → 5
nums = [3,2,3,1,2,4,5,5,6], k = 4  → 4
```

**Constraints**
* `1 <= k <= nums.length <= 10^5`; `-10^4 <= nums[i] <= 10^4`

## Solutions

Each folder below is a separate, self-contained Gradle project, ordered from the simplest idea to the most efficient one.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-sort](v1-sort/README.md) | Sort | `O(n log n)` | `O(log n)` | [▶ animation](v1-sort/animation/index.html) |
| [v2-min-heap-of-size-k](v2-min-heap-of-size-k/README.md) | Min-heap of size k | `O(n log k)` | `O(k)` | [▶ animation](v2-min-heap-of-size-k/animation/index.html) |
| [v3-quickselect](v3-quickselect/README.md) | Quickselect | `O(n)` | `O(1)` | [▶ animation](v3-quickselect/animation/index.html) |
