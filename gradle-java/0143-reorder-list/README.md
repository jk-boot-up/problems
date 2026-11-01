# 143. Reorder List

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Linked List &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/reorder-list/)

## Problem

Reorder `L0 → L1 → … → Ln` into `L0 → Ln → L1 → Ln-1 → L2 → …` in place (re-link nodes, do not change values).

**Example**
```
1 → 2 → 3 → 4       becomes 1 → 4 → 2 → 3
1 → 2 → 3 → 4 → 5   becomes 1 → 5 → 2 → 4 → 3
```

**Constraints**
* `1 <= n <= 5 * 10^4`

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-split-reverse-merge](v1-split-reverse-merge/README.md) | Split, reverse, merge | `O(n)` | `O(1)` | [▶ animation](v1-split-reverse-merge/animation/index.html) |
