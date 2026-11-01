# 389. Find the Difference

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Bit Manipulation &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/find-the-difference/)

## Problem

`t` is `s` shuffled with one extra letter added. Return that letter.

**Example**
```
s = "abcd", t = "abcde" → 'e',   s = "", t = "y" → 'y'
```

**Constraints**
* `0 <= s.length <= 1000`; `t.length == s.length + 1`

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-xor-of-characters](v1-xor-of-characters/README.md) | XOR of characters | `O(n)` | `O(1)` | [▶ animation](v1-xor-of-characters/animation/index.html) |
