# 2390. Removing Stars From a String

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Stack &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/removing-stars-from-a-string/)

## Problem

Each `*` in `s` removes itself and the closest non-star character to its left. Return the string after all stars are processed (the input
always allows this).

**Example**
```
"leet**cod*e" → "lecoe",   "erase*****" → ""
```

**Constraints**
* `1 <= s.length <= 10^5`

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-stack-via-stringbuilder](v1-stack-via-stringbuilder/README.md) | Stack via StringBuilder | `O(n)` | `O(n)` | [▶ animation](v1-stack-via-stringbuilder/animation/index.html) |
