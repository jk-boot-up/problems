# 12. Integer to Roman

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Array / String &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/integer-to-roman/)

## Problem

Convert an integer `num` (1 to 3999) to a Roman numeral. Use the standard symbols `I, V, X, L, C, D, M` and the
subtractive forms `IV, IX, XL, XC, CD, CM`. `I`, `X`, `C` and `M` may repeat up to three times in a row; `V`, `L` and `D` never repeat.

**Example 1**
```
Input:  num = 3749
Output: "MMMDCCXLIX"
```

**Example 2**
```
Input:  num = 58
Output: "LVIII"
```

**Constraints**
* `1 <= num <= 3999`

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-greedy-value-table](v1-greedy-value-table/README.md) | Greedy value table | `O(1)` | `O(1)` | [▶ animation](v1-greedy-value-table/animation/index.html) |
