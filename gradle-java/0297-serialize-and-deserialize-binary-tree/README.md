# 297. Serialize and Deserialize Binary Tree

**Difficulty:** Hard &nbsp;|&nbsp; **Topic:** Binary Tree General &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/serialize-and-deserialize-binary-tree/)

## Problem

Design `serialize(TreeNode)` → `String` and `deserialize(String)` → `TreeNode` so that deserializing a serialized tree reproduces it
exactly. Any format is allowed.

**Example**
```
[1,2,3,null,null,4,5] → "1,2,#,#,3,4,#,#,5,#,#" → [1,2,3,null,null,4,5]
```

**Constraints**
* `0 <= n <= 10^4`; `-1000 <= Node.val <= 1000`

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-preorder-with-null-markers](v1-preorder-with-null-markers/README.md) | Preorder with null markers | `O(n)` | `O(n)` | [▶ animation](v1-preorder-with-null-markers/animation/index.html) |
