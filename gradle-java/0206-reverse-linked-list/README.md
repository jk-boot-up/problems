# 206. Reverse Linked List

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Linked List &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/reverse-linked-list/)

## Problem

Reverse a singly linked list and return the new head.

**Example**
```
1 → 2 → 3 → 4 → 5   becomes   5 → 4 → 3 → 2 → 1
```

**Constraints**
* `0 <= n <= 5000`

**Follow-up:** do it both iteratively and recursively.

## Solutions

Each folder below is a separate, self-contained Gradle project, ordered from the simplest idea to the most efficient one.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-recursive](v1-recursive/README.md) | Recursive | `O(n)` | `O(n)` | [▶ animation](v1-recursive/animation/index.html) |
| [v2-iterative-pointer-reversal](v2-iterative-pointer-reversal/README.md) | Iterative pointer reversal | `O(n)` | `O(1)` | [▶ animation](v2-iterative-pointer-reversal/animation/index.html) |
