# 1249. Minimum Remove to Make Valid Parentheses

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Stack &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/)

## Problem

Remove the minimum number of parentheses from `s` (letters stay) so that the result is valid. Return any valid result.

**Example**
```
"lee(t(c)o)de)" → "lee(t(c)o)de"
"a)b(c)d"       → "ab(c)d"
"))(("          → ""
```

**Constraints**
* `1 <= s.length <= 10^5`

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-stack-of-open-indices](v1-stack-of-open-indices/README.md) | Stack of open indices | `O(n)` | `O(n)` | [▶ animation](v1-stack-of-open-indices/animation/index.html) |
