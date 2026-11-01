# 117. Populating Next Right Pointers in Each Node II

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Binary Tree General &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/)

## Problem

Each node of a binary tree has an extra pointer `next`. Set every `next` to the node immediately to its right on the same level, or
to `null` if there is none. The tree is not necessarily perfect.

**Example**
```
Input:  [1,2,3,4,5,null,7]
Output: levels linked as  1 → null,  2 → 3 → null,  4 → 5 → 7 → null
```

**Constraints**
* `0 <= n <= 6000`; `-100 <= Node.val <= 100`

**Follow-up:** constant extra space (the recursion stack does not count).

## Solutions

Each folder below is a separate, self-contained Gradle project, ordered from the simplest idea to the most efficient one.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-bfs-with-a-queue](v1-bfs-with-a-queue/README.md) | BFS with a queue | `O(n)` | `O(w)` | [▶ animation](v1-bfs-with-a-queue/animation/index.html) |
| [v2-level-walk-with-o-1-space](v2-level-walk-with-o-1-space/README.md) | Level walk with O(1) space | `O(n)` | `O(1)` | [▶ animation](v2-level-walk-with-o-1-space/animation/index.html) |
