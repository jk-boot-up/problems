# 101. Symmetric Tree

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Binary Tree General &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/symmetric-tree/)

## Problem

Return `true` if a binary tree is a mirror of itself (symmetric around its centre).

**Example 1**
```
Input:  [1,2,2,3,4,4,3]
Output: true
```

**Example 2**
```
Input:  [1,2,2,null,3,null,3]
Output: false
```

**Constraints**
* `1 <= n <= 1000`; `-100 <= Node.val <= 100`

## Solutions

Each folder below is a separate, self-contained Gradle project, ordered from the simplest idea to the most efficient one.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-iterative-queue-of-pairs](v1-iterative-queue-of-pairs/README.md) | Iterative queue of pairs | `O(n)` | `O(w)` | [▶ animation](v1-iterative-queue-of-pairs/animation/index.html) |
| [v2-recursive-mirror-check](v2-recursive-mirror-check/README.md) | Recursive mirror check | `O(n)` | `O(h)` | [▶ animation](v2-recursive-mirror-check/animation/index.html) |
