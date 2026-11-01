# 328. Odd Even Linked List

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Linked List &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/odd-even-linked-list/)

## Problem

Group all nodes at **odd positions** (1st, 3rd, …) first, followed by nodes at even positions, keeping relative order within each group.
Use O(1) extra space and O(n) time.

**Example**
```
1 → 2 → 3 → 4 → 5        becomes 1 → 3 → 5 → 2 → 4
2 → 1 → 3 → 5 → 6 → 4 → 7 becomes 2 → 3 → 6 → 7 → 1 → 5 → 4
```

**Constraints**
* `0 <= n <= 10^4`

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-two-interleaved-chains](v1-two-interleaved-chains/README.md) | Two interleaved chains | `O(n)` | `O(1)` | [▶ animation](v1-two-interleaved-chains/animation/index.html) |
