# 225. Implement Stack using Queues

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Design &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/implement-stack-using-queues/)

## Problem

Implement a LIFO stack (`push`, `pop`, `top`, `empty`) using only queue operations (add to back, remove/peek from front, size, isEmpty).

**Example**
```
push(1); push(2); top() → 2; pop() → 2; empty() → false
```

**Constraints**
* At most 100 calls; `pop`/`top` are only called on a non-empty stack.

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-one-queue-with-rotation](v1-one-queue-with-rotation/README.md) | One queue with rotation | `O(n)` | `O(n)` | [▶ animation](v1-one-queue-with-rotation/animation/index.html) |
