# 337. House Robber III

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Binary Tree General &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/house-robber-iii/)

## Problem

Houses form a binary tree; robbing two directly-linked houses (parent and child) triggers the alarm. Return the maximum amount you can rob.

**Example**
```
[3,2,3,null,3,null,1] → 7   (3 + 3 + 1)
[3,4,5,1,3,null,1]    → 9   (4 + 5)
```

**Constraints**
* `1 <= n <= 10^4`

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-post-order-pair-dp](v1-post-order-pair-dp/README.md) | Post-order pair DP | `O(n)` | `O(h)` | [▶ animation](v1-post-order-pair-dp/animation/index.html) |
