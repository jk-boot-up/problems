# 23. Merge k Sorted Lists

**Difficulty:** Hard &nbsp;|&nbsp; **Topic:** Divide & Conquer &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/merge-k-sorted-lists/)

## Problem

You are given an array of `k` linked lists, each sorted ascending. Merge them into one sorted linked list and return its head.

**Example**
```
Input:  [[1,4,5],[1,3,4],[2,6]]
Output: 1 → 1 → 2 → 3 → 4 → 4 → 5 → 6
```

**Constraints**
* `0 <= k <= 10^4`; total nodes `N <= 10^4`

## Solutions

Each folder below is a separate, self-contained Gradle project, ordered from the simplest idea to the most efficient one.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-min-heap-of-list-heads](v1-min-heap-of-list-heads/README.md) | Min-heap of list heads | `O(N log k)` | `O(k)` | [▶ animation](v1-min-heap-of-list-heads/animation/index.html) |
| [v2-pairwise-divide-and-conquer](v2-pairwise-divide-and-conquer/README.md) | Pairwise divide and conquer | `O(N log k)` | `O(1)` | [▶ animation](v2-pairwise-divide-and-conquer/animation/index.html) |
