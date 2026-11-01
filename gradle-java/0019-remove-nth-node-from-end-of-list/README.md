# 19. Remove Nth Node From End of List

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Linked List &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/remove-nth-node-from-end-of-list/)

## Problem

Remove the `n`-th node from the **end** of the list and return its head.

**Example 1**
```
Input:  head = 1 → 2 → 3 → 4 → 5, n = 2
Output: 1 → 2 → 3 → 5
```

**Example 2**
```
Input:  head = 1, n = 1
Output: (empty)
```

**Constraints**
* `1 <= sz <= 30`; `1 <= n <= sz`

**Follow-up:** one pass.

## Solutions

Each folder below is a separate, self-contained Gradle project, ordered from the simplest idea to the most efficient one.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-count-length-then-remove](v1-count-length-then-remove/README.md) | Count length, then remove | `O(L)` | `O(1)` | [▶ animation](v1-count-length-then-remove/animation/index.html) |
| [v2-one-pass-gap-of-n](v2-one-pass-gap-of-n/README.md) | One pass, gap of n | `O(L)` | `O(1)` | [▶ animation](v2-one-pass-gap-of-n/animation/index.html) |
