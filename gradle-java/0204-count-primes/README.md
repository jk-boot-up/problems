# 204. Count Primes

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Math &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/count-primes/)

## Problem

Return the number of prime numbers **strictly less than** `n`.

**Example**
```
10 → 4    (2, 3, 5, 7)
0  → 0
1  → 0
```

**Constraints**
* `0 <= n <= 5 * 10^6`

## Solutions

Each folder below is a separate, self-contained Gradle project, ordered from the simplest idea to the most efficient one.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-trial-division](v1-trial-division/README.md) | Trial division | `O(n√n)` | `O(1)` | [▶ animation](v1-trial-division/animation/index.html) |
| [v2-sieve-of-eratosthenes](v2-sieve-of-eratosthenes/README.md) | Sieve of Eratosthenes | `O(n log log n)` | `O(n)` | [▶ animation](v2-sieve-of-eratosthenes/animation/index.html) |
