# 42. Trapping Rain Water

**Difficulty:** Hard &nbsp;|&nbsp; **Topic:** Array / String &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/trapping-rain-water/)

## Problem

`height[i]` is the height of a bar of width 1. After it rains, how many units of water are trapped between the bars?

**Example 1**
```
Input:  height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
```

**Example 2**
```
Input:  height = [4,2,0,3,2,5]
Output: 9
```

**Constraints**
* `1 <= n <= 2 * 10^4`
* `0 <= height[i] <= 10^5`

## Solutions

Each folder below is a separate, self-contained Gradle project, ordered from the simplest idea to the most efficient one.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-prefix-suffix-maximum-arrays](v1-prefix-suffix-maximum-arrays/README.md) | Prefix / suffix maximum arrays | `O(n)` | `O(n)` | [▶ animation](v1-prefix-suffix-maximum-arrays/animation/index.html) |
| [v2-two-pointers](v2-two-pointers/README.md) | Two pointers | `O(n)` | `O(1)` | [▶ animation](v2-two-pointers/animation/index.html) |
