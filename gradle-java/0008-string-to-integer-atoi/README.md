# 8. String to Integer (atoi)

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Strings &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/string-to-integer-atoi/)

## Problem

Convert a string to a 32-bit signed integer:
1. skip leading spaces; 2. read an optional `+` or `-`; 3. read digits until a non-digit (ignore the rest);
4. if no digits were read the result is 0; 5. clamp to `[-2^31, 2^31 - 1]`.

**Example**
```
"42" → 42,   "   -042" → -42,   "1337c0d3" → 1337,   "0-1" → 0,   "words and 987" → 0
```

**Constraints**
* `0 <= s.length <= 200`

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-single-pass-with-clamping](v1-single-pass-with-clamping/README.md) | Single pass with clamping | `O(n)` | `O(1)` | [▶ animation](v1-single-pass-with-clamping/animation/index.html) |
