# 1209. Remove All Adjacent Duplicates in String II

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Stack &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/)

## Problem

Repeatedly remove `k` adjacent equal letters from `s` until no such group remains. Return the final string.

**Example**
```
s = "abcd",                 k = 2 → "abcd"
s = "deeedbbcccbdaa",       k = 3 → "aa"
s = "pbbcggttciiippooaais", k = 2 → "ps"
```

**Constraints**
* `1 <= s.length <= 10^5`, `2 <= k <= 10^4`

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-stack-of-runs](v1-stack-of-runs/README.md) | Stack of runs | `O(n)` | `O(n)` | [▶ animation](v1-stack-of-runs/animation/index.html) |
