# 224. Basic Calculator

**Difficulty:** Hard &nbsp;|&nbsp; **Topic:** Stack &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/basic-calculator/)

## Problem

Evaluate a valid expression string `s` containing non-negative integers, `+`, `-`, parentheses and spaces. `-` may also be unary
(e.g. `"-(2 + 3)"`). Do not use `eval`.

**Example 1**
```
Input:  s = "1 + 1"
Output: 2
```

**Example 2**
```
Input:  s = " 2-1 + 2 "
Output: 3
```

**Example 3**
```
Input:  s = "(1+(4+5+2)-3)+(6+8)"
Output: 23
```

**Constraints**
* `1 <= s.length <= 3 * 10^5`; the result and intermediate values fit in 32-bit integers.

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-sign-stack](v1-sign-stack/README.md) | Sign stack | `O(n)` | `O(n)` | [▶ animation](v1-sign-stack/animation/index.html) |
