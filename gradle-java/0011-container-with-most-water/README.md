# 11. Container With Most Water

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Two Pointers &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/container-with-most-water/)

## Problem

`height[i]` is the height of a vertical line at position `i`. Choose two lines that, together with the x-axis, form a container
holding the most water. Return that maximum amount: `min(height[i], height[j]) × (j - i)`.

**Example 1**
```
Input:  height = [1,8,6,2,5,4,8,3,7]
Output: 49   (lines at 1 and 8: min(8,7) × 7)
```

**Example 2**
```
Input:  height = [1,1]
Output: 1
```

**Constraints**
* `2 <= n <= 10^5`
* `0 <= height[i] <= 10^4`

## Solutions

Each folder below is a separate, self-contained Gradle project, ordered from the simplest idea to the most efficient one.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-brute-force](v1-brute-force/README.md) | Brute force | `O(n²)` | `O(1)` | [▶ animation](v1-brute-force/animation/index.html) |
| [v2-two-pointers](v2-two-pointers/README.md) | Two pointers | `O(n)` | `O(1)` | [▶ animation](v2-two-pointers/animation/index.html) |
