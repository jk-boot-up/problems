# 6. Zigzag Conversion

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Array / String &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/zigzag-conversion/)

## Problem

Write the string `s` in a zigzag pattern on `numRows` rows (down the rows, then diagonally back up, and repeat), then read it
row by row. For `"PAYPALISHIRING"` with 3 rows:
```
P   A   H   N
A P L S I I G
Y   I   R
```
which reads `"PAHNAPLSIIGYIR"`.

**Example 1**
```
Input:  s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
```

**Example 2**
```
Input:  s = "A", numRows = 1
Output: "A"
```

**Constraints**
* `1 <= s.length <= 1000`, `1 <= numRows <= 1000`

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-row-simulation](v1-row-simulation/README.md) | Row simulation | `O(n)` | `O(n)` | [▶ animation](v1-row-simulation/animation/index.html) |
