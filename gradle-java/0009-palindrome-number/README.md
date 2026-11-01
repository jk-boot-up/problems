# 9. Palindrome Number

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Math &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/palindrome-number/)

## Problem

Return `true` if the integer `x` reads the same forward and backward.

**Example**
```
121 → true,   -121 → false (reads 121-),   10 → false
```

**Constraints**
* `-2^31 <= x <= 2^31 - 1`

**Follow-up:** solve it without converting to a string.

## Solutions

Each folder below is a separate, self-contained Gradle project, ordered from the simplest idea to the most efficient one.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-compare-as-a-string](v1-compare-as-a-string/README.md) | Compare as a string | `O(log n)` | `O(log n)` | [▶ animation](v1-compare-as-a-string/animation/index.html) |
| [v2-reverse-half-the-digits](v2-reverse-half-the-digits/README.md) | Reverse half the digits | `O(log n)` | `O(1)` | [▶ animation](v2-reverse-half-the-digits/animation/index.html) |
