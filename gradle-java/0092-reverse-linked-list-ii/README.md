# 92. Reverse Linked List II

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Linked List &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/reverse-linked-list-ii/)

## Problem

Given the `head` of a singly linked list and positions `left <= right` (1-based), reverse the nodes from position `left` to
`right` and return the list.

**Example 1**
```
Input:  head = 1 → 2 → 3 → 4 → 5, left = 2, right = 4
Output: 1 → 4 → 3 → 2 → 5
```

**Example 2**
```
Input:  head = 5, left = 1, right = 1
Output: 5
```

**Constraints**
* `1 <= n <= 500`; `1 <= left <= right <= n`

**Follow-up:** one pass.

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-one-pass-head-insertion](v1-one-pass-head-insertion/README.md) | One pass, head insertion | `O(n)` | `O(1)` | [▶ animation](v1-one-pass-head-insertion/animation/index.html) |
