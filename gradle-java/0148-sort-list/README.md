# 148. Sort List

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Divide & Conquer &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/sort-list/)

## Problem

Sort a linked list in ascending order and return its head.

**Example**
```
Input:  4 → 2 → 1 → 3
Output: 1 → 2 → 3 → 4
```

**Constraints**
* `0 <= n <= 5 * 10^4`; `-10^5 <= Node.val <= 10^5`

**Follow-up:** O(n log n) time and O(1) memory.

## Solutions

Each folder below is a separate, self-contained Gradle project, ordered from the simplest idea to the most efficient one.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-top-down-merge-sort](v1-top-down-merge-sort/README.md) | Top-down merge sort | `O(n log n)` | `O(log n)` | [▶ animation](v1-top-down-merge-sort/animation/index.html) |
| [v2-bottom-up-merge-sort-o-1-space](v2-bottom-up-merge-sort-o-1-space/README.md) | Bottom-up merge sort (O(1) space) | `O(n log n)` | `O(1)` | [▶ animation](v2-bottom-up-merge-sort-o-1-space/animation/index.html) |
