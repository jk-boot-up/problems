# 295. Find Median from Data Stream

**Difficulty:** Hard &nbsp;|&nbsp; **Topic:** Heap &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/find-median-from-data-stream/)

## Problem

Implement `MedianFinder`:
* `addNum(int num)`: add a number from the stream;
* `double findMedian()`: the median of all numbers so far (the mean of the two middle values for an even count).

**Example**
```
addNum(1), addNum(2) → findMedian() = 1.5; addNum(3) → findMedian() = 2.0
```

**Constraints**
* `-10^5 <= num <= 10^5`; up to `5 * 10^4` calls; `findMedian` is called on a non-empty stream.

## Solutions

Each folder below is a separate, self-contained Gradle project, ordered from the simplest idea to the most efficient one.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-sorted-list-with-binary-insertion](v1-sorted-list-with-binary-insertion/README.md) | Sorted list with binary insertion | `O(n)` | `O(n)` | [▶ animation](v1-sorted-list-with-binary-insertion/animation/index.html) |
| [v2-two-heaps](v2-two-heaps/README.md) | Two heaps | `O(log n)` | `O(n)` | [▶ animation](v2-two-heaps/animation/index.html) |
