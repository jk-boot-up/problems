# 51. N-Queens

**Difficulty:** Hard &nbsp;|&nbsp; **Topic:** Backtracking &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/n-queens/)

## Problem

Return all distinct solutions to the `n`-queens puzzle as boards of strings, where `'Q'` is a queen and `'.'` an empty square.

**Example**
```
n = 4 → [[".Q..","...Q","Q...","..Q."], ["..Q.","Q...","...Q",".Q.."]]
```

**Constraints**
* `1 <= n <= 9`

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-backtracking-with-attack-sets](v1-backtracking-with-attack-sets/README.md) | Backtracking with attack sets | `O(n!)` | `O(n)` | [▶ animation](v1-backtracking-with-attack-sets/animation/index.html) |
