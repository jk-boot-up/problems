# 653. Two Sum IV - Input is a BST

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Binary Search Tree &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/two-sum-iv-input-is-a-bst/)

## Problem

Return `true` if two different nodes of the BST have values summing to `k`.

**Example**
```
root = [5,3,6,2,4,null,7], k = 9 → true,   k = 28 → false
```

**Constraints**
* `1 <= n <= 10^4`

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-dfs-with-a-seen-set](v1-dfs-with-a-seen-set/README.md) | DFS with a seen set | `O(n)` | `O(n)` | [▶ animation](v1-dfs-with-a-seen-set/animation/index.html) |
