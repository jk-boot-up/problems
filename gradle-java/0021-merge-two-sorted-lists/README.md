# 21. Merge Two Sorted Lists

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Linked List &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/merge-two-sorted-lists/)

## Problem

Merge two sorted linked lists `list1` and `list2` into one sorted list by splicing their nodes together. Return its head.

**Example 1**
```
Input:  list1 = 1 → 2 → 4, list2 = 1 → 3 → 4
Output: 1 → 1 → 2 → 3 → 4 → 4
```

**Example 2**
```
Input:  list1 = null, list2 = 0
Output: 0
```

**Constraints**
* `0..50` nodes per list; `-100 <= Node.val <= 100`; both sorted non-decreasing.

## Solutions

Each folder below is a separate, self-contained Gradle project, ordered from the simplest idea to the most efficient one.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-recursive](v1-recursive/README.md) | Recursive | `O(m + n)` | `O(m + n)` | [▶ animation](v1-recursive/animation/index.html) |
| [v2-iterative-with-dummy-head](v2-iterative-with-dummy-head/README.md) | Iterative with dummy head | `O(m + n)` | `O(1)` | [▶ animation](v2-iterative-with-dummy-head/animation/index.html) |
