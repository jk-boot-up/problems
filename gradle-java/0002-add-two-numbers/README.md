# 2. Add Two Numbers

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Linked List &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/add-two-numbers/)

## Problem

Two non-negative integers are stored as linked lists with their digits in **reverse order** (ones digit first), one digit per node.
Return their sum as a linked list in the same format. Neither number has leading zeros, except the number 0 itself.

**Example 1**
```
Input:  l1 = 2 → 4 → 3, l2 = 5 → 6 → 4    (342 + 465)
Output: 7 → 0 → 8                         (807)
```

**Example 2**
```
Input:  l1 = 9 → 9 → 9 → 9, l2 = 9 → 9
Output: 8 → 9 → 0 → 0 → 1
```

**Constraints**
* Each list has `1..100` nodes; `0 <= Node.val <= 9`.

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-digit-by-digit-with-carry](v1-digit-by-digit-with-carry/README.md) | Digit-by-digit with carry | `O(max(m, n))` | `O(1)` | [▶ animation](v1-digit-by-digit-with-carry/animation/index.html) |
