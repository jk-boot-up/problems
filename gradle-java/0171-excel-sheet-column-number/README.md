# 171. Excel Sheet Column Number

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Math &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/excel-sheet-column-number/)

## Problem

Given a column title as shown in a spreadsheet, return its column number (`A → 1`, `Z → 26`, `AA → 27`, …).

**Example**
```
"A"  → 1
"AB" → 28
"ZY" → 701
```

**Constraints**
* `1 <= columnTitle.length <= 7`, upper-case letters, value at most `2^31 - 1`

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-horner-s-rule-in-base-26](v1-horner-s-rule-in-base-26/README.md) | Horner's rule in base 26 | `O(n)` | `O(1)` | [▶ animation](v1-horner-s-rule-in-base-26/animation/index.html) |
