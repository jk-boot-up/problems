# 20. Valid Parentheses

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Stack &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/valid-parentheses/)

## Problem

Given a string `s` of the characters `()[]{}`, decide whether it is **valid**: every opening bracket is closed by the same type of
bracket, in the correct order, and every closing bracket has a matching opener.

**Example 1**
```
Input:  s = "()[]{}"
Output: true
```

**Example 2**
```
Input:  s = "(]"
Output: false
```

**Example 3**
```
Input:  s = "([])"
Output: true
```

**Constraints**
* `1 <= s.length <= 10^4`; only `()[]{}`.

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-stack-of-openers](v1-stack-of-openers/README.md) | Stack of openers | `O(n)` | `O(n)` | [▶ animation](v1-stack-of-openers/animation/index.html) |
