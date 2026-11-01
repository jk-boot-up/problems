# 392. Is Subsequence

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Two Pointers &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/is-subsequence/)

## Problem

Return `true` if `s` is a **subsequence** of `t`: that is, `s` can be formed by deleting some (possibly zero) characters
of `t` without changing the order of the rest.

**Example 1**
```
Input:  s = "abc", t = "ahbgdc"
Output: true
```

**Example 2**
```
Input:  s = "axc", t = "ahbgdc"
Output: false
```

**Constraints**
* `0 <= s.length <= 100`, `0 <= t.length <= 10^4`, lowercase letters only.

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-two-pointers](v1-two-pointers/README.md) | Two pointers | `O(n)` | `O(1)` | [▶ animation](v1-two-pointers/animation/index.html) |
