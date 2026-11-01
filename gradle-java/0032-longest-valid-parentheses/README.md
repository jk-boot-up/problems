# 32. Longest Valid Parentheses

**Difficulty:** Hard &nbsp;|&nbsp; **Topic:** Stack &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/longest-valid-parentheses/)

## Problem

Given a string of `'('` and `')'`, return the length of the longest **well-formed** (valid) parentheses substring.

**Example**
```
"(()" → 2,   ")()())" → 4,   "" → 0
```

**Constraints**
* `0 <= s.length <= 3 * 10^4`

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-index-stack-with-sentinel](v1-index-stack-with-sentinel/README.md) | Index stack with sentinel | `O(n)` | `O(n)` | [▶ animation](v1-index-stack-with-sentinel/animation/index.html) |
