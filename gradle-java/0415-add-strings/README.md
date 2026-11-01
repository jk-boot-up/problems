# 415. Add Strings

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Math &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/add-strings/)

## Problem

Given two non-negative integers as strings, return their sum as a string, without converting the inputs to numbers.

**Example**
```
"11"  + "123" → "134"
"456" + "77"  → "533"
"0"   + "0"   → "0"
```

**Constraints**
* `1 <= length <= 10^4`; no leading zeros except `"0"`

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-digit-by-digit-with-carry](v1-digit-by-digit-with-carry/README.md) | Digit-by-digit with carry | `O(max(m, n))` | `O(max(m, n))` | [▶ animation](v1-digit-by-digit-with-carry/animation/index.html) |
