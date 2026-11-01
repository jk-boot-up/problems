# 844. Backspace String Compare

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Two Pointers &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/backspace-string-compare/)

## Problem

`#` is a backspace. Return `true` if `s` and `t` are equal after typing both into empty editors.

**Example**
```
"ab#c", "ad#c" → true,   "ab##", "c#d#" → true,   "a#c", "b" → false
```

**Constraints**
* `1 <= s.length, t.length <= 200`

**Follow-up:** O(n) time and O(1) space.

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-backward-two-pointers](v1-backward-two-pointers/README.md) | Backward two pointers | `O(m + n)` | `O(1)` | [▶ animation](v1-backward-two-pointers/animation/index.html) |
