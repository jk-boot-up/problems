# 301. Remove Invalid Parentheses

**Difficulty:** Hard &nbsp;|&nbsp; **Topic:** Backtracking &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/remove-invalid-parentheses/)

## Problem

Remove the **minimum** number of parentheses to make the string valid. Return every distinct valid result, in any order. Letters stay.

**Example**
```
"()())()"  → ["(())()","()()()"]
"(a)())()" → ["(a())()","(a)()()"]
")("       → [""]
```

**Constraints**
* `1 <= s.length <= 25`; `s` has letters and parentheses, at most 20 parentheses

## Solutions

Each folder below is a separate, self-contained Gradle project, ordered from the simplest idea to the most efficient one.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-bfs-by-number-of-removals](v1-bfs-by-number-of-removals/README.md) | BFS by number of removals | `O(2ⁿ · n)` | `O(2ⁿ · n)` | [▶ animation](v1-bfs-by-number-of-removals/animation/index.html) |
| [v2-dfs-with-counted-removals](v2-dfs-with-counted-removals/README.md) | DFS with counted removals | `O(2ⁿ · n)` | `O(n²)` | [▶ animation](v2-dfs-with-counted-removals/animation/index.html) |
