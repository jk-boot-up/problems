# 382. Linked List Random Node

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Randomized &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/linked-list-random-node/)

## Problem

Given a singly linked list, implement `getRandom()` returning the value of a node chosen uniformly at random. Each node must be equally
likely.

* `LinkedListRandomNode(ListNode head)`
* `int getRandom()`

**Example**
```
list [1,2,3]: getRandom() returns 1, 2 or 3, each with probability 1/3
```

**Constraints**
* `1 <= n <= 10^4`; up to `10^4` calls
* Follow-up: what if the list is huge and its length unknown? Use O(1) extra space.

## Solutions

Each folder below is a separate, self-contained Gradle project, ordered from the simplest idea to the most efficient one.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-copy-into-an-array](v1-copy-into-an-array/README.md) | Copy into an array | `O(1)` | `O(n)` | [▶ animation](v1-copy-into-an-array/animation/index.html) |
| [v2-reservoir-sampling](v2-reservoir-sampling/README.md) | Reservoir sampling | `O(n)` | `O(1)` | [▶ animation](v2-reservoir-sampling/animation/index.html) |
