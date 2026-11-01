# 232. Implement Queue using Stacks

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Design &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/implement-queue-using-stacks/)

## Problem

Implement a FIFO queue (`push`, `pop`, `peek`, `empty`) using only two stacks (push to top, pop/peek from top, size, isEmpty).

**Example**
```
push(1); push(2); peek() → 1; pop() → 1; empty() → false
```

**Constraints**
* At most 100 calls; `pop`/`peek` are only called on a non-empty queue.

**Follow-up:** amortized O(1) per operation.

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-two-stacks-lazy-transfer](v1-two-stacks-lazy-transfer/README.md) | Two stacks, lazy transfer | `O(1)` | `O(n)` | [▶ animation](v1-two-stacks-lazy-transfer/animation/index.html) |
