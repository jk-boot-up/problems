# 703. Kth Largest Element in a Stream

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Heap &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/kth-largest-element-in-a-stream/)

## Problem

Implement `KthLargest(k, nums)` and `int add(val)`, which adds `val` to the stream and returns the current `k`-th largest element.

**Example**
```
KthLargest(3, [4,5,8,2]); add(3) → 4; add(5) → 5; add(10) → 5; add(9) → 8; add(4) → 8
```

**Constraints**
* `1 <= k <= 10^4`; at least `k` elements exist when `add` returns.

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-min-heap-of-size-k](v1-min-heap-of-size-k/README.md) | Min-heap of size k | `O(log k)` | `O(k)` | [▶ animation](v1-min-heap-of-size-k/animation/index.html) |
