# 1544. Make The String Great

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Stack &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/make-the-string-great/)

## Problem

A string is **good** if no two adjacent characters are the same letter in different cases (like `"aA"`). Repeatedly remove such adjacent
pairs and return the resulting string (possibly empty).

**Example**
```
"leEeetcode" → "leetcode"
"abBAcC"     → ""
"s"          → "s"
```

**Constraints**
* `1 <= s.length <= 100`, English letters

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-stack-of-letters](v1-stack-of-letters/README.md) | Stack of letters | `O(n)` | `O(n)` | [▶ animation](v1-stack-of-letters/animation/index.html) |
