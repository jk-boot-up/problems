# 374. Guess Number Higher or Lower

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Binary Search &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/guess-number-higher-or-lower/)

## Problem

A number `pick` is chosen from `1..n`. The API `guess(num)` returns `-1` if `num > pick`, `1` if `num < pick`, `0` if correct. Return `pick`.
(Here the API is a method of the same class, initialised with the hidden pick.)

**Example**
```
n = 10, pick = 6 → 6,   n = 1, pick = 1 → 1
```

**Constraints**
* `1 <= pick <= n <= 2^31 - 1`

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-binary-search-on-the-hint](v1-binary-search-on-the-hint/README.md) | Binary search on the hint | `O(log n)` | `O(1)` | [▶ animation](v1-binary-search-on-the-hint/animation/index.html) |
