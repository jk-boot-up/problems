# 52. N-Queens II

**Difficulty:** Hard &nbsp;|&nbsp; **Topic:** Backtracking &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/n-queens-ii/)

## Problem

Place `n` queens on an `n × n` chessboard so that no two attack each other (no shared row, column or diagonal). Return the number of
distinct solutions.

**Example**
```
Input:  n = 4
Output: 2
```

**Constraints**
* `1 <= n <= 9`

## Solutions

Each folder below is a separate, self-contained Gradle project, ordered from the simplest idea to the most efficient one.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-boolean-arrays](v1-boolean-arrays/README.md) | Boolean arrays | `O(n!)` | `O(n)` | [▶ animation](v1-boolean-arrays/animation/index.html) |
| [v2-bitmask-backtracking](v2-bitmask-backtracking/README.md) | Bitmask backtracking | `O(n!)` | `O(n)` | [▶ animation](v2-bitmask-backtracking/animation/index.html) |
