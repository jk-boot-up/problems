# 46. Permutations

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Backtracking &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/permutations/)

## Problem

Given an array `nums` of **distinct** integers, return all possible permutations, in any order.

**Example**
```
Input:  nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,2,1],[3,1,2]]
```

**Constraints**
* `1 <= nums.length <= 6`; values are distinct.

## Solutions

Each folder below is a separate, self-contained Gradle project, ordered from the simplest idea to the most efficient one.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-path-with-used-flags](v1-path-with-used-flags/README.md) | Path with used flags | `O(n · n!)` | `O(n)` | [▶ animation](v1-path-with-used-flags/animation/index.html) |
| [v2-in-place-swapping](v2-in-place-swapping/README.md) | In-place swapping | `O(n · n!)` | `O(n)` | [▶ animation](v2-in-place-swapping/animation/index.html) |
