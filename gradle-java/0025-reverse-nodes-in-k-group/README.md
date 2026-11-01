# 25. Reverse Nodes in k-Group

**Difficulty:** Hard &nbsp;|&nbsp; **Topic:** Linked List &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/reverse-nodes-in-k-group/)

## Problem

Reverse the nodes of a linked list `k` at a time and return the new head. If the number of remaining nodes is less than `k`,
leave them as they are. Only change the links, not the values.

**Example 1**
```
Input:  head = 1 → 2 → 3 → 4 → 5, k = 2
Output: 2 → 1 → 4 → 3 → 5
```

**Example 2**
```
Input:  head = 1 → 2 → 3 → 4 → 5, k = 3
Output: 3 → 2 → 1 → 4 → 5
```

**Constraints**
* `1 <= k <= n <= 5000`

**Follow-up:** O(1) extra memory.

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-iterative-group-reversal](v1-iterative-group-reversal/README.md) | Iterative group reversal | `O(n)` | `O(1)` | [▶ animation](v1-iterative-group-reversal/animation/index.html) |
