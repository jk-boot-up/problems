# 456. 132 Pattern

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Monotonic Stack &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/132-pattern/)

## Problem

Return `true` if there are indices `i < j < k` with `nums[i] < nums[k] < nums[j]` (a "132" shape).

**Example**
```
[1,2,3,4]  → false
[3,1,4,2]  → true    (1, 4, 2)
[-1,3,2,0] → true
```

**Constraints**
* `1 <= nums.length <= 2 * 10^5`

## Solutions

Each folder below is a separate, self-contained Gradle project, ordered from the simplest idea to the most efficient one.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-prefix-minimum-check-every-pair](v1-prefix-minimum-check-every-pair/README.md) | Prefix minimum, check every pair | `O(n²)` | `O(1)` | [▶ animation](v1-prefix-minimum-check-every-pair/animation/index.html) |
| [v2-monotonic-stack-from-the-right](v2-monotonic-stack-from-the-right/README.md) | Monotonic stack from the right | `O(n)` | `O(n)` | [▶ animation](v2-monotonic-stack-from-the-right/animation/index.html) |
