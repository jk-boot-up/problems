# 2095. Delete the Middle Node of a Linked List

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Linked List &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/)

## Problem

Delete the middle node (index `⌊n/2⌋`, 0-based) of a linked list and return the head.

**Example**
```
1→3→4→7→1→2→6 becomes 1→3→4→1→2→6,   1→2→3→4 becomes 1→2→4,   2→1 becomes 2
```

**Constraints**
* `1 <= n <= 10^5`

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-slow-and-fast-pointers](v1-slow-and-fast-pointers/README.md) | Slow and fast pointers | `O(n)` | `O(1)` | [▶ animation](v1-slow-and-fast-pointers/animation/index.html) |
