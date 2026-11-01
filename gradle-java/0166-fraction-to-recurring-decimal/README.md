# 166. Fraction to Recurring Decimal

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Hash Map &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/fraction-to-recurring-decimal/)

## Problem

Given two integers `numerator` and `denominator`, return the fraction as a string. If the fractional part repeats, wrap the repeating
part in parentheses.

**Example**
```
1 / 2    → "0.5"
2 / 1    → "2"
4 / 333  → "0.(012)"
1 / 6    → "0.1(6)"
-50 / 8  → "-6.25"
```

**Constraints**
* `-2^31 <= numerator, denominator <= 2^31 - 1`, `denominator != 0`

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-long-division-with-a-remainder-map](v1-long-division-with-a-remainder-map/README.md) | Long division with a remainder map | `O(d)` | `O(d)` | [▶ animation](v1-long-division-with-a-remainder-map/animation/index.html) |
