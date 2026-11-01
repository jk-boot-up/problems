# 650. 2 Keys Keyboard

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Math &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/2-keys-keyboard/)

## Problem

The screen starts with one `'A'`. Each step is either **Copy All** (copy everything on screen) or **Paste** (append the last copy). Return
the minimum number of steps to get exactly `n` letters.

**Example**
```
n = 3 → 3   (copy, paste, paste)
n = 1 → 0
n = 6 → 5   (copy, paste → 2; copy, paste, paste → 6)
```

**Constraints**
* `1 <= n <= 1000`

## Solutions

Each folder below is a separate, self-contained Gradle project, ordered from the simplest idea to the most efficient one.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-dynamic-programming-over-divisors](v1-dynamic-programming-over-divisors/README.md) | Dynamic programming over divisors | `O(n²)` | `O(n)` | [▶ animation](v1-dynamic-programming-over-divisors/animation/index.html) |
| [v2-sum-of-prime-factors](v2-sum-of-prime-factors/README.md) | Sum of prime factors | `O(√n)` | `O(1)` | [▶ animation](v2-sum-of-prime-factors/animation/index.html) |
