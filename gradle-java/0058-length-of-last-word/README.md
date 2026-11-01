# 58. Length of Last Word

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Array / String &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/length-of-last-word/)

## Problem

Given a string `s` of words and spaces, return the length of the **last** word. A word is a maximal run of non-space characters.

**Example 1**
```
Input:  s = "Hello World"
Output: 5
```

**Example 2**
```
Input:  s = "   fly me   to   the moon  "
Output: 4
```

**Constraints**
* `1 <= s.length <= 10^4`
* `s` has only English letters and spaces, and at least one word.

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-backward-scan](v1-backward-scan/README.md) | Backward scan | `O(n)` | `O(1)` | [▶ animation](v1-backward-scan/animation/index.html) |
