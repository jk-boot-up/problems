# 67. Add Binary

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Bit Manipulation &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/add-binary/)

## Problem

Given two binary strings `a` and `b`, return their sum as a binary string.

**Example**
```
a = "11",   b = "1"    → "100"
a = "1010", b = "1011" → "10101"
```

**Constraints**
* `1 <= a.length, b.length <= 10^4`; no leading zeros except "0" itself.

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-right-to-left-with-carry](v1-right-to-left-with-carry/README.md) | Right-to-left with carry | `O(max(m, n))` | `O(max(m, n))` | [▶ animation](v1-right-to-left-with-carry/animation/index.html) |
