# 61. Rotate List

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Linked List &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/rotate-list/)

## Problem

Rotate a linked list to the right by `k` places and return the new head.

**Example 1**
```
Input:  1 → 2 → 3 → 4 → 5, k = 2
Output: 4 → 5 → 1 → 2 → 3
```

**Example 2**
```
Input:  0 → 1 → 2, k = 4
Output: 2 → 0 → 1
```

**Constraints**
* `0 <= n <= 500`; `0 <= k <= 2 * 10^9`

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-ring-and-cut](v1-ring-and-cut/README.md) | Ring and cut | `O(n)` | `O(1)` | [▶ animation](v1-ring-and-cut/animation/index.html) |
