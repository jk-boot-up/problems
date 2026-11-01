# 168. Excel Sheet Column Title

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Math &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/excel-sheet-column-title/)

## Problem

Given a positive integer `columnNumber`, return its column title as it appears in a spreadsheet: `1 → A`, `26 → Z`, `27 → AA`,
`28 → AB`, …

**Example**
```
1   → "A"
28  → "AB"
701 → "ZY"
```

**Constraints**
* `1 <= columnNumber <= 2^31 - 1`

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-bijective-base-26](v1-bijective-base-26/README.md) | Bijective base-26 | `O(log₂₆ n)` | `O(1)` | [▶ animation](v1-bijective-base-26/animation/index.html) |
