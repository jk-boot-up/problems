# 445. Add Two Numbers II

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Linked List &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/add-two-numbers-ii/)

## Problem

Two non-empty linked lists hold non-negative integers with the **most significant digit first**. Return their sum as a list in the same
order, without reversing the input lists.

**Example**
```
[7,2,4,3] + [5,6,4] → [7,8,0,7]    (7243 + 564 = 7807)
[2,4,3]   + [5,6,4] → [8,0,7]
[0] + [0]           → [0]
```

**Constraints**
* `1 <= length <= 100`; no leading zeros except the number 0

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-two-stacks](v1-two-stacks/README.md) | Two stacks | `O(m + n)` | `O(m + n)` | [▶ animation](v1-two-stacks/animation/index.html) |
