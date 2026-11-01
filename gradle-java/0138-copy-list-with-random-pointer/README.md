# 138. Copy List with Random Pointer

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Linked List &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/copy-list-with-random-pointer/)

## Problem

Each node of a linked list has `val`, `next`, and `random`, which points to any node in the list or `null`. Return a **deep copy**:
new nodes with the same values whose `next` and `random` pointers mirror the original structure, never pointing into the original list.

**Example**
```
Input:  [[7,null],[13,0],[11,4],[10,2],[1,0]]   ([val, index of random])
Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]   (a separate copy)
```

**Constraints**
* `0 <= n <= 1000`; `-10^4 <= Node.val <= 10^4`

## Solutions

Each folder below is a separate, self-contained Gradle project, ordered from the simplest idea to the most efficient one.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-old-to-new-hash-map](v1-old-to-new-hash-map/README.md) | Old-to-new hash map | `O(n)` | `O(n)` | [▶ animation](v1-old-to-new-hash-map/animation/index.html) |
| [v2-interleaved-copies](v2-interleaved-copies/README.md) | Interleaved copies | `O(n)` | `O(1)` | [▶ animation](v2-interleaved-copies/animation/index.html) |
