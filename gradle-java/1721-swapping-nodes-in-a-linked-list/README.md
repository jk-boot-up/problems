# 1721. Swapping Nodes in a Linked List

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Linked List &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/swapping-nodes-in-a-linked-list/)

## Problem

Swap the **values** of the `k`-th node from the beginning and the `k`-th node from the end (1-indexed) and return the head.

**Example**
```
head = [1,2,3,4,5], k = 2 → [1,4,3,2,5]
head = [7,9,6,6,7,8,3,0,9,5], k = 5 → [7,9,6,6,8,7,3,0,9,5]
```

**Constraints**
* `1 <= k <= n <= 10^5`

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-two-pointers-swap-values](v1-two-pointers-swap-values/README.md) | Two pointers, swap values | `O(n)` | `O(1)` | [▶ animation](v1-two-pointers-swap-values/animation/index.html) |
