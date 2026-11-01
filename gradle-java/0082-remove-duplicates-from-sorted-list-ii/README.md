# 82. Remove Duplicates from Sorted List II

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Linked List &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/)

## Problem

Given the head of a **sorted** linked list, delete every node whose value appears more than once, leaving only values that were
distinct in the original list. Return the sorted result.

**Example 1**
```
Input:  1 → 2 → 3 → 3 → 4 → 4 → 5
Output: 1 → 2 → 5
```

**Example 2**
```
Input:  1 → 1 → 1 → 2 → 3
Output: 2 → 3
```

**Constraints**
* `0 <= n <= 300`; sorted ascending.

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-skip-whole-runs](v1-skip-whole-runs/README.md) | Skip whole runs | `O(n)` | `O(1)` | [▶ animation](v1-skip-whole-runs/animation/index.html) |
