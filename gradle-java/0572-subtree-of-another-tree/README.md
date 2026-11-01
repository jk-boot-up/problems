# 572. Subtree of Another Tree

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Binary Tree General &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/subtree-of-another-tree/)

## Problem

Return `true` if `subRoot` appears in `root` as a **subtree**: some node of `root` together with all its descendants is identical to
`subRoot`.

**Example**
```
root = [3,4,5,1,2], subRoot = [4,1,2]                       → true
root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2] → false
```

**Constraints**
* `1 <= n <= 2000`; `1 <= m <= 1000`

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-same-tree-check-at-every-node](v1-same-tree-check-at-every-node/README.md) | Same-tree check at every node | `O(n·m)` | `O(h)` | [▶ animation](v1-same-tree-check-at-every-node/animation/index.html) |
