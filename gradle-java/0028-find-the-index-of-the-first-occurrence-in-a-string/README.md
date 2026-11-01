# 28. Find the Index of the First Occurrence in a String

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Array / String &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/)

## Problem

Return the index of the first occurrence of `needle` in `haystack`, or `-1` if `needle` does not occur.

**Example 1**
```
Input:  haystack = "sadbutsad", needle = "sad"
Output: 0
```

**Example 2**
```
Input:  haystack = "leetcode", needle = "leeto"
Output: -1
```

**Constraints**
* `1 <= haystack.length, needle.length <= 10^4`, lowercase letters only.

## Solutions

Each folder below is a separate, self-contained Gradle project, ordered from the simplest idea to the most efficient one.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-brute-force](v1-brute-force/README.md) | Brute force | `O(n·m)` | `O(1)` | [▶ animation](v1-brute-force/animation/index.html) |
| [v2-kmp](v2-kmp/README.md) | KMP | `O(n + m)` | `O(m)` | [▶ animation](v2-kmp/animation/index.html) |
