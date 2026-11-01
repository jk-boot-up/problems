# 227. Basic Calculator II

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Stack &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/basic-calculator-ii/)

## Problem

Evaluate an expression string containing non-negative integers, `+ - * /` and spaces. Integer division truncates toward zero. The
expression is always valid and every intermediate value fits in 32 bits. Do not use `eval`.

**Example**
```
"3+2*2"      → 7
" 3/2 "      → 1
" 3+5 / 2 "  → 5
```

**Constraints**
* `1 <= s.length <= 3 * 10^5`

## Solutions

Each folder below is a separate, self-contained Gradle project, ordered from the simplest idea to the most efficient one.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-stack-of-terms](v1-stack-of-terms/README.md) | Stack of terms | `O(n)` | `O(n)` | [▶ animation](v1-stack-of-terms/animation/index.html) |
| [v2-running-sum-with-the-last-term](v2-running-sum-with-the-last-term/README.md) | Running sum with the last term | `O(n)` | `O(1)` | [▶ animation](v2-running-sum-with-the-last-term/animation/index.html) |
