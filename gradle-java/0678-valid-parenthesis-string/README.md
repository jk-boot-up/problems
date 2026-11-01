# 678. Valid Parenthesis String

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Greedy &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/valid-parenthesis-string/)

## Problem

`s` contains `(`, `)` and `*`, where `*` can be `(`, `)` or empty. Return `true` if some choice makes `s` a valid parentheses string.

**Example**
```
"()" → true,   "(*)" → true,   "(*))" → true,   ")(" → false
```

**Constraints**
* `1 <= s.length <= 100`

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-range-of-open-counts](v1-range-of-open-counts/README.md) | Range of open counts | `O(n)` | `O(1)` | [▶ animation](v1-range-of-open-counts/animation/index.html) |
