# 307. Range Sum Query - Mutable

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Fenwick Tree &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/range-sum-query-mutable/)

## Problem

Implement `NumArray` supporting both updates and range sums:

* `NumArray(int[] nums)`
* `void update(int index, int val)` — set `nums[index] = val`.
* `int sumRange(int left, int right)` — the sum of `nums[left..right]`.

**Example**
```
nums = [1,3,5]
sumRange(0,2) → 9, update(1,2), sumRange(0,2) → 8
```

**Constraints**
* `1 <= nums.length <= 3 * 10^4`, up to `3 * 10^4` calls

## Solutions

Each folder below is a separate, self-contained Gradle project, ordered from the simplest idea to the most efficient one.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-plain-array-sum-on-demand](v1-plain-array-sum-on-demand/README.md) | Plain array, sum on demand | `O(n)` | `O(n)` | [▶ animation](v1-plain-array-sum-on-demand/animation/index.html) |
| [v2-fenwick-binary-indexed-tree](v2-fenwick-binary-indexed-tree/README.md) | Fenwick (binary indexed) tree | `O(log n)` | `O(n)` | [▶ animation](v2-fenwick-binary-indexed-tree/animation/index.html) |
