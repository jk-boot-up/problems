# 258. Add Digits

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Math &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/add-digits/)

## Problem

Given a non-negative integer `num`, repeatedly add its digits until one digit remains, and return it.

**Example**
```
38 → 3 + 8 = 11 → 1 + 1 = 2
0  → 0
```

**Constraints**
* `0 <= num <= 2^31 - 1`

## Solutions

Each folder below is a separate, self-contained Gradle project, ordered from the simplest idea to the most efficient one.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-repeated-digit-sums](v1-repeated-digit-sums/README.md) | Repeated digit sums | `O(log n)` | `O(1)` | [▶ animation](v1-repeated-digit-sums/animation/index.html) |
| [v2-digital-root-formula](v2-digital-root-formula/README.md) | Digital root formula | `O(1)` | `O(1)` | [▶ animation](v2-digital-root-formula/animation/index.html) |
