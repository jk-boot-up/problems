# 264. Ugly Number II

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Dynamic Programming &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/ugly-number-ii/)

## Problem

Return the `n`-th ugly number (prime factors only 2, 3 and 5; the sequence starts `1, 2, 3, 4, 5, 6, 8, 9, 10, 12, …`).

**Example**
```
n = 10 → 12
n = 1  → 1
```

**Constraints**
* `1 <= n <= 1690`

## Solutions

Each folder below is a separate, self-contained Gradle project, ordered from the simplest idea to the most efficient one.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-min-heap-with-a-seen-set](v1-min-heap-with-a-seen-set/README.md) | Min-heap with a seen set | `O(n log n)` | `O(n)` | [▶ animation](v1-min-heap-with-a-seen-set/animation/index.html) |
| [v2-three-pointers](v2-three-pointers/README.md) | Three pointers | `O(n)` | `O(n)` | [▶ animation](v2-three-pointers/animation/index.html) |
