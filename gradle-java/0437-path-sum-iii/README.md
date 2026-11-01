# 437. Path Sum III

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Binary Tree General &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/path-sum-iii/)

## Problem

Count the downward paths (from a node to one of its descendants, not necessarily root or leaf) whose values sum to `targetSum`.

**Example**
```
root = [10,5,-3,3,2,null,11,3,-2,null,1], targetSum = 8 → 3
```

**Constraints**
* `0 <= n <= 1000`; sums may need 64 bits.

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-prefix-sums-on-the-path](v1-prefix-sums-on-the-path/README.md) | Prefix sums on the path | `O(n)` | `O(h)` | [▶ animation](v1-prefix-sums-on-the-path/animation/index.html) |
