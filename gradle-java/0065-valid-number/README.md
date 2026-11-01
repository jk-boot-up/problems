# 65. Valid Number

**Difficulty:** Hard &nbsp;|&nbsp; **Topic:** Strings &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/valid-number/)

## Problem

Return `true` if `s` is a valid number: an integer or decimal (optional sign, digits with at most one dot and at least one digit), optionally
followed by `e`/`E` and an integer exponent (optional sign, at least one digit).

**Example**
```
valid:   "2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10", "-90E3", "3e+7", "53.5e93"
invalid: "abc", "1a", "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53", "."
```

**Constraints**
* `1 <= s.length <= 20`

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-single-scan-with-flags](v1-single-scan-with-flags/README.md) | Single scan with flags | `O(n)` | `O(1)` | [▶ animation](v1-single-scan-with-flags/animation/index.html) |
