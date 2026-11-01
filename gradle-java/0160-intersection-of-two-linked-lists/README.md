# 160. Intersection of Two Linked Lists

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Linked List &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/intersection-of-two-linked-lists/)

## Problem

Two singly linked lists may merge into a shared tail. Return the first shared **node**, or `null` if they do not intersect. Do not modify
the lists.

**Example**
```
A: 4 → 1 ↘
            8 → 4 → 5
B: 5 → 6 → 1 ↗          → the node with value 8
```

**Constraints**
* `1 <= m, n <= 3 * 10^4`

**Follow-up:** O(m + n) time and O(1) memory.

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-switching-pointers](v1-switching-pointers/README.md) | Switching pointers | `O(m + n)` | `O(1)` | [▶ animation](v1-switching-pointers/animation/index.html) |
