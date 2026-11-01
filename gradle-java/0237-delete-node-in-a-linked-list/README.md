# 237. Delete Node in a Linked List

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Linked List &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/delete-node-in-a-linked-list/)

## Problem

You are given only a reference to a node in a singly linked list (not the head). The node is not the tail and all values are unique.
Delete that node's value from the list: afterwards the list should read the same as before, minus that value.

**Example**
```
head = [4,5,1,9], node = 5 → [4,1,9]
head = [4,5,1,9], node = 1 → [4,5,9]
```

**Constraints**
* `2 <= n <= 1000`; the given node is not the last one

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-copy-the-next-node](v1-copy-the-next-node/README.md) | Copy the next node | `O(1)` | `O(1)` | [▶ animation](v1-copy-the-next-node/animation/index.html) |
