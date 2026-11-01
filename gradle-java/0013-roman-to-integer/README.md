# 13. Roman to Integer

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Array / String &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/roman-to-integer/)

## Problem

Roman numerals use `I=1, V=5, X=10, L=50, C=100, D=500, M=1000`. Symbols are usually written largest to smallest,
except for six subtractive pairs: `IV=4, IX=9, XL=40, XC=90, CD=400, CM=900`. Convert a valid Roman numeral `s` to an integer.

**Example 1**
```
Input:  s = "LVIII"
Output: 58
```

**Example 2**
```
Input:  s = "MCMXCIV"
Output: 1994   (M + CM + XC + IV)
```

**Constraints**
* `1 <= s.length <= 15`
* `s` is a valid Roman numeral in the range `[1, 3999]`.

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-look-one-ahead](v1-look-one-ahead/README.md) | Look one ahead | `O(n)` | `O(1)` | [▶ animation](v1-look-one-ahead/animation/index.html) |
