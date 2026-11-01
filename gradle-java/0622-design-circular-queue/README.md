# 622. Design Circular Queue

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Design &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/design-circular-queue/)

## Problem

Implement a fixed-capacity circular queue:

* `MyCircularQueue(int k)`
* `boolean enQueue(int value)`, `boolean deQueue()` — return `false` when full / empty.
* `int Front()`, `int Rear()` — return `-1` when empty.
* `boolean isEmpty()`, `boolean isFull()`

**Example**
```
k = 3: enQueue(1) true, enQueue(2) true, enQueue(3) true, enQueue(4) false,
Rear() 3, isFull() true, deQueue() true, enQueue(4) true, Rear() 4
```

**Constraints**
* `1 <= k <= 1000`, up to 3000 calls

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-array-with-head-and-size](v1-array-with-head-and-size/README.md) | Array with head and size | `O(1)` | `O(k)` | [▶ animation](v1-array-with-head-and-size/animation/index.html) |
