# 86. Partition List

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Linked List &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/partition-list/)

## Problem

Given the head of a linked list and a value `x`, rearrange it so that all nodes **less than** `x` come before nodes greater than or
equal to `x`. Keep the original relative order inside each part.

**Example 1**
```
Input:  1 → 4 → 3 → 2 → 5 → 2, x = 3
Output: 1 → 2 → 2 → 4 → 3 → 5
```

**Example 2**
```
Input:  2 → 1, x = 2
Output: 1 → 2
```

**Constraints**
* `0 <= n <= 200`; `-100 <= Node.val <= 100`; `-200 <= x <= 200`

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-two-chains](v1-two-chains/README.md) | Two chains | `O(n)` | `O(1)` | [▶ animation](v1-two-chains/animation/index.html) |
