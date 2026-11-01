# 2336. Smallest Number in Infinite Set

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Heap &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/smallest-number-in-infinite-set/)

## Problem

The set initially contains every positive integer. Implement:
* `popSmallest()`: remove and return the smallest number;
* `addBack(num)`: put `num` back if it is not already in the set.

**Example**
```
addBack(2); popSmallest() → 1; popSmallest() → 2; popSmallest() → 3;
addBack(1); popSmallest() → 1; popSmallest() → 4; popSmallest() → 5
```

**Constraints**
* `1 <= num <= 1000`; at most 1000 calls.

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-counter-min-heap-of-returned-numbers](v1-counter-min-heap-of-returned-numbers/README.md) | Counter + min-heap of returned numbers | `O(log n)` | `O(n)` | [▶ animation](v1-counter-min-heap-of-returned-numbers/animation/index.html) |
