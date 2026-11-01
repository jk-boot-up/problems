# 141. Linked List Cycle

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Linked List &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/linked-list-cycle/)

## Problem

Given the `head` of a linked list, return `true` if the list has a **cycle**: some node can be reached again by following `next`.

**Example 1**
```
Input:  3 → 2 → 0 → -4 → (back to 2)
Output: true
```

**Example 2**
```
Input:  1 → 2 → null
Output: false
```

**Constraints**
* `0 <= number of nodes <= 10^4`

**Follow-up:** O(1) memory.

## Solutions

Each folder below is a separate, self-contained Gradle project, ordered from the simplest idea to the most efficient one.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-visited-node-set](v1-visited-node-set/README.md) | Visited-node set | `O(n)` | `O(n)` | [▶ animation](v1-visited-node-set/animation/index.html) |
| [v2-floyd-fast-and-slow-pointers](v2-floyd-fast-and-slow-pointers/README.md) | Floyd fast and slow pointers | `O(n)` | `O(1)` | [▶ animation](v2-floyd-fast-and-slow-pointers/animation/index.html) |
