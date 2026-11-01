# 150. Evaluate Reverse Polish Notation

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Stack &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/evaluate-reverse-polish-notation/)

## Problem

Evaluate an arithmetic expression in **Reverse Polish Notation** given as `tokens`. Operators are `+ - * /`; each operand is an
integer or a sub-expression. Division truncates toward zero. The expression is always valid and fits in 32-bit integers.

**Example 1**
```
Input:  tokens = ["2","1","+","3","*"]
Output: 9   ((2 + 1) * 3)
```

**Example 2**
```
Input:  tokens = ["4","13","5","/","+"]
Output: 6   (4 + 13 / 5)
```

**Constraints**
* `1 <= tokens.length <= 10^4`

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-operand-stack](v1-operand-stack/README.md) | Operand stack | `O(n)` | `O(n)` | [▶ animation](v1-operand-stack/animation/index.html) |
