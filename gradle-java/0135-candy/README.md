# 135. Candy

**Difficulty:** Hard &nbsp;|&nbsp; **Topic:** Array / String &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/candy/)

## Problem

`n` children stand in a line; `ratings[i]` is child `i`'s rating. Give out candies so that:
* every child gets at least one candy, and
* a child with a higher rating than a neighbour gets more candies than that neighbour.

Return the minimum total number of candies.

**Example 1**
```
Input:  ratings = [1,0,2]
Output: 5   (2, 1, 2)
```

**Example 2**
```
Input:  ratings = [1,2,2]
Output: 4   (1, 2, 1)
```

**Constraints**
* `1 <= n <= 2 * 10^4`
* `0 <= ratings[i] <= 2 * 10^4`

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-two-passes](v1-two-passes/README.md) | Two passes | `O(n)` | `O(n)` | [▶ animation](v1-two-passes/animation/index.html) |
