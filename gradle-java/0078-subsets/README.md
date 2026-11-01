# 78. Subsets

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Backtracking &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/subsets/)

## Problem

Given an array of **unique** integers, return all possible subsets (the power set), in any order, without duplicates.

**Example**
```
[1,2,3] → [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
```

**Constraints**
* `1 <= nums.length <= 10`

## Solutions

Each folder below is a separate, self-contained Gradle project, ordered from the simplest idea to the most efficient one.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-bitmask-enumeration](v1-bitmask-enumeration/README.md) | Bitmask enumeration | `O(n · 2ⁿ)` | `O(n)` | [▶ animation](v1-bitmask-enumeration/animation/index.html) |
| [v2-backtracking](v2-backtracking/README.md) | Backtracking | `O(n · 2ⁿ)` | `O(n)` | [▶ animation](v2-backtracking/animation/index.html) |
