# 303. Range Sum Query - Immutable

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Prefix Sum &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/range-sum-query-immutable/)

## Problem

Implement `NumArray`:

* `NumArray(int[] nums)`
* `int sumRange(int left, int right)` — the sum of `nums[left..right]` inclusive.

**Example**
```
nums = [-2,0,3,-5,2,-1]
sumRange(0,2) → 1, sumRange(2,5) → -1, sumRange(0,5) → -3
```

**Constraints**
* `1 <= nums.length <= 10^4`, up to `10^4` queries

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-prefix-sums](v1-prefix-sums/README.md) | Prefix sums | `O(1)` | `O(n)` | [▶ animation](v1-prefix-sums/animation/index.html) |
