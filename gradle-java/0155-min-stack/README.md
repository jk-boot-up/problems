# 155. Min Stack

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Stack &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/min-stack/)

## Problem

Design a stack that supports `push(val)`, `pop()`, `top()` and `getMin()` (the smallest element in the stack), each in **O(1)** time.
`pop`, `top` and `getMin` are only called on a non-empty stack.

**Example**
```
push(-2), push(0), push(-3)
getMin() → -3
pop()
top()    → 0
getMin() → -2
```

**Constraints**
* `-2^31 <= val <= 2^31 - 1`; at most `3 * 10^4` calls.

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-value-and-minimum-pairs](v1-value-and-minimum-pairs/README.md) | Value-and-minimum pairs | `O(1)` | `O(n)` | [▶ animation](v1-value-and-minimum-pairs/animation/index.html) |
