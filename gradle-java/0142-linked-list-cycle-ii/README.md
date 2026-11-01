# 142. Linked List Cycle II

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Linked List &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/linked-list-cycle-ii/)

## Problem

Return the node where the cycle in a linked list begins, or `null` if there is no cycle. Do not modify the list.

**Example**
```
3 → 2 → 0 → -4 → (back to 2)   → the node with value 2
1 → 2 → (back to 1)            → the node with value 1
```

**Constraints**
* `0 <= n <= 10^4`

**Follow-up:** O(1) memory.

## Solutions

Each folder below is a separate, self-contained Gradle project, ordered from the simplest idea to the most efficient one.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-visited-node-set](v1-visited-node-set/README.md) | Visited-node set | `O(n)` | `O(n)` | [▶ animation](v1-visited-node-set/animation/index.html) |
| [v2-floyd-meet-then-find-the-entrance](v2-floyd-meet-then-find-the-entrance/README.md) | Floyd: meet, then find the entrance | `O(n)` | `O(1)` | [▶ animation](v2-floyd-meet-then-find-the-entrance/animation/index.html) |
