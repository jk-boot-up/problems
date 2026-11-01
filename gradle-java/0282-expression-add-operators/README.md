# 282. Expression Add Operators

**Difficulty:** Hard &nbsp;|&nbsp; **Topic:** Backtracking &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/expression-add-operators/)

## Problem

Given a digit string `num` and an integer `target`, insert `+`, `-` or `*` between digits (or nothing, to join digits into one number) and
return every expression that evaluates to `target`. Numbers must not have leading zeros (`"05"` is not allowed, `"0"` is).

**Example**
```
num = "123", target = 6   → ["1*2*3","1+2+3"]
num = "232", target = 8   → ["2*3+2","2+3*2"]
num = "105", target = 5   → ["1*0+5","10-5"]
num = "3456237490", target = 9191 → []
```

**Constraints**
* `1 <= num.length <= 10`, `-2^31 <= target <= 2^31 - 1`

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-backtracking-with-the-last-operand](v1-backtracking-with-the-last-operand/README.md) | Backtracking with the last operand | `O(4ⁿ · n)` | `O(n)` | [▶ animation](v1-backtracking-with-the-last-operand/animation/index.html) |
