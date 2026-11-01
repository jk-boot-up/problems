# 229. Majority Element II

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Arrays & Hashing &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/majority-element-ii/)

## Problem

Return all values that appear **more than ⌊n/3⌋ times** in `nums`, in any order.

**Example**
```
[3,2,3] → [3],   [1] → [1],   [1,2] → [1,2]
```

**Constraints**
* `1 <= nums.length <= 5 * 10^4`

**Follow-up:** O(n) time and O(1) space.

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-two-candidate-voting](v1-two-candidate-voting/README.md) | Two-candidate voting | `O(n)` | `O(1)` | [▶ animation](v1-two-candidate-voting/animation/index.html) |
