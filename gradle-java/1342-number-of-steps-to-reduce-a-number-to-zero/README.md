# 1342. Number of Steps to Reduce a Number to Zero

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Bit Manipulation &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/)

## Problem

Repeatedly halve `num` if it is even, or subtract 1 if it is odd, until it is 0. Return the number of steps.

**Example**
```
14 → 6,   8 → 4,   123 → 12
```

**Constraints**
* `0 <= num <= 10^6`

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-simulation](v1-simulation/README.md) | Simulation | `O(log n)` | `O(1)` | [▶ animation](v1-simulation/animation/index.html) |
