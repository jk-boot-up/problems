# 1047. Remove All Adjacent Duplicates In String

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Stack &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/)

## Problem

Repeatedly remove two adjacent equal letters from `s` until no such pair remains. Return the final string (it is unique).

**Example**
```
"abbaca" → "ca",   "azxxzy" → "ay"
```

**Constraints**
* `1 <= s.length <= 10^5`

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-stack-via-stringbuilder](v1-stack-via-stringbuilder/README.md) | Stack via StringBuilder | `O(n)` | `O(n)` | [▶ animation](v1-stack-via-stringbuilder/animation/index.html) |
