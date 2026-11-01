# 24. Swap Nodes in Pairs

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Linked List &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/swap-nodes-in-pairs/)

## Problem

Swap every two adjacent nodes of a linked list and return its head. Change the links, not the values.

**Example**
```
1 → 2 → 3 → 4 becomes 2 → 1 → 4 → 3,   1 stays 1,   (empty) stays empty
```

**Constraints**
* `0 <= n <= 100`

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-iterative-re-linking](v1-iterative-re-linking/README.md) | Iterative re-linking | `O(n)` | `O(1)` | [▶ animation](v1-iterative-re-linking/animation/index.html) |
