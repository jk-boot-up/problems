# 1071. Greatest Common Divisor of Strings

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Math &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/greatest-common-divisor-of-strings/)

## Problem

`t` divides `s` if `s` is `t` repeated some number of times. Return the largest string that divides both `str1` and `str2`, or `""`.

**Example**
```
"ABCABC", "ABC" → "ABC",   "ABABAB", "ABAB" → "AB",   "LEET", "CODE" → ""
```

**Constraints**
* `1 <= str1.length, str2.length <= 1000`; uppercase letters.

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-concatenation-check-gcd](v1-concatenation-check-gcd/README.md) | Concatenation check + gcd | `O(m + n)` | `O(m + n)` | [▶ animation](v1-concatenation-check-gcd/animation/index.html) |
