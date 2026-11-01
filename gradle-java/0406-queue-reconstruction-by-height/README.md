# 406. Queue Reconstruction by Height

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Greedy &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/queue-reconstruction-by-height/)

## Problem

Each person is `[h, k]`: height `h`, and exactly `k` people **in front** of them have height `>= h`. Reconstruct the queue from a shuffled
list.

**Example**
```
[[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]] → [[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]]
```

**Constraints**
* `1 <= n <= 2000`; a valid queue always exists

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-sort-tall-first-insert-at-k](v1-sort-tall-first-insert-at-k/README.md) | Sort tall-first, insert at k | `O(n²)` | `O(n)` | [▶ animation](v1-sort-tall-first-insert-at-k/animation/index.html) |
