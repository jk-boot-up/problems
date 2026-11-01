# 313. Super Ugly Number

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Dynamic Programming &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/super-ugly-number/)

## Problem

A **super ugly number** is a positive integer whose prime factors all appear in the array `primes`. Return the `n`-th super ugly number
(1 is the first). The answer fits in a 32-bit signed integer.

**Example**
```
n = 12, primes = [2,7,13,19] → 32
   (1,2,4,7,8,13,14,16,19,26,28,32)
n = 1,  primes = [2,3,5]     → 1
```

**Constraints**
* `1 <= n <= 10^5`, `1 <= primes.length <= 100`, primes are distinct and sorted

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-one-pointer-per-prime](v1-one-pointer-per-prime/README.md) | One pointer per prime | `O(n · k)` | `O(n + k)` | [▶ animation](v1-one-pointer-per-prime/animation/index.html) |
