# 257. Binary Tree Paths

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Binary Tree DFS &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/binary-tree-paths/)

## Problem

Return all root-to-leaf paths of a binary tree, in any order, written as `"a->b->c"`.

**Example**
```
[1,2,3,null,5] → ["1->2->5","1->3"]
[1]            → ["1"]
```

**Constraints**
* `1 <= n <= 100`

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-dfs-carrying-the-path](v1-dfs-carrying-the-path/README.md) | DFS carrying the path | `O(n · h)` | `O(h)` | [▶ animation](v1-dfs-carrying-the-path/animation/index.html) |
