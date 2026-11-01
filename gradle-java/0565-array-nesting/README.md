# 565. Array Nesting

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Array &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/array-nesting/)

## Problem

`nums` is a permutation of `0..n-1`. Starting at `k`, build `s[k] = {nums[k], nums[nums[k]], …}` until a value repeats. Return the size of
the largest `s[k]`.

**Example**
```
[5,4,0,3,1,6,2] → 4   (0 → 5 → 6 → 2 → 0)
[0,1,2]         → 1
```

**Constraints**
* `1 <= nums.length <= 10^5`

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-walk-each-cycle-once](v1-walk-each-cycle-once/README.md) | Walk each cycle once | `O(n)` | `O(n)` | [▶ animation](v1-walk-each-cycle-once/animation/index.html) |
