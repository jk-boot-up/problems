# 1318. Minimum Flips to Make a OR b Equal to c

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Bit Manipulation &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/minimum-flips-to-make-a-or-b-equal-to-c/)

## Problem

Return the minimum number of single-bit flips in `a` and `b` so that `a | b == c`.

**Example**
```
a = 2, b = 6, c = 5 → 3,   a = 4, b = 2, c = 7 → 1,   a = 1, b = 2, c = 3 → 0
```

**Constraints**
* `1 <= a, b, c <= 10^9`

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-per-bit-counting](v1-per-bit-counting/README.md) | Per-bit counting | `O(1)` | `O(1)` | [▶ animation](v1-per-bit-counting/animation/index.html) |
