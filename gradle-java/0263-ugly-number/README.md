# 263. Ugly Number

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Math &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/ugly-number/)

## Problem

An **ugly number** is a positive integer whose only prime factors are 2, 3 and 5. Return `true` if `n` is ugly. (1 counts as ugly.)

**Example**
```
6  → true   (2 × 3)
1  → true
14 → false  (has the factor 7)
```

**Constraints**
* `-2^31 <= n <= 2^31 - 1`

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-divide-out-2-3-and-5](v1-divide-out-2-3-and-5/README.md) | Divide out 2, 3 and 5 | `O(log n)` | `O(1)` | [▶ animation](v1-divide-out-2-3-and-5/animation/index.html) |
