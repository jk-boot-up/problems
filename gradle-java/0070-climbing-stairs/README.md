# 70. Climbing Stairs

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** 1D DP &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/climbing-stairs/)

## Problem

You climb a staircase of `n` steps, taking 1 or 2 steps at a time. In how many distinct ways can you reach the top?

**Example**
```
n = 2 → 2 (1+1, 2),   n = 3 → 3 (1+1+1, 1+2, 2+1)
```

**Constraints**
* `1 <= n <= 45`

## Solutions

Each folder below is a separate, self-contained Gradle project, ordered from the simplest idea to the most efficient one.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-memoized-recursion](v1-memoized-recursion/README.md) | Memoized recursion | `O(n)` | `O(n)` | [▶ animation](v1-memoized-recursion/animation/index.html) |
| [v2-two-rolling-variables](v2-two-rolling-variables/README.md) | Two rolling variables | `O(n)` | `O(1)` | [▶ animation](v2-two-rolling-variables/animation/index.html) |
