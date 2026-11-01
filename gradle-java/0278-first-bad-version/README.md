# 278. First Bad Version

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Binary Search &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/first-bad-version/)

## Problem

Versions `1..n` were released in order. Once a version is bad, every later version is bad too. Given an API `isBadVersion(v)`, find the
first bad version while calling the API as few times as possible.

In this project the API is passed to the constructor as an `IntPredicate`.

**Example**
```
n = 5, first bad = 4 → 4   (isBad(3) = false, isBad(5) = true, isBad(4) = true)
n = 1, first bad = 1 → 1
```

**Constraints**
* `1 <= bad <= n <= 2^31 - 1`

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-binary-search-for-the-boundary](v1-binary-search-for-the-boundary/README.md) | Binary search for the boundary | `O(log n)` | `O(1)` | [▶ animation](v1-binary-search-for-the-boundary/animation/index.html) |
