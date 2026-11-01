# 1381. Design a Stack With Increment Operation

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Design &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/design-a-stack-with-increment-operation/)

## Problem

Implement `CustomStack`:

* `CustomStack(int maxSize)` — pushes beyond `maxSize` elements are ignored.
* `void push(int x)`, `int pop()` (returns `-1` when empty).
* `void increment(int k, int val)` — add `val` to the bottom `k` elements (all of them if fewer).

**Example**
```
CustomStack(3); push(1); push(2); pop() → 2; push(2); push(3); push(4) (ignored);
increment(5,100); increment(2,100); pop() → 103; pop() → 202; pop() → 201; pop() → -1
```

**Constraints**
* `1 <= maxSize, x, k <= 1000`; up to 1000 calls of each method

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-lazy-increments](v1-lazy-increments/README.md) | Lazy increments | `O(1)` | `O(maxSize)` | [▶ animation](v1-lazy-increments/animation/index.html) |
