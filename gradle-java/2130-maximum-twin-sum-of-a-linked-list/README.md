# 2130. Maximum Twin Sum of a Linked List

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Linked List &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/)

## Problem

In a linked list of even length `n`, node `i` and node `n - 1 - i` are twins. Return the maximum twin sum.

**Example**
```
5→4→2→1 → 6,   4→2→2→3 → 7,   1→100000 → 100001
```

**Constraints**
* `n` is even, `2 <= n <= 10^5`

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-reverse-second-half](v1-reverse-second-half/README.md) | Reverse second half | `O(n)` | `O(1)` | [▶ animation](v1-reverse-second-half/animation/index.html) |
