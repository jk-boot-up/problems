# 567. Permutation in String

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Sliding Window &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/permutation-in-string/)

## Problem

Return `true` if `s2` contains a permutation of `s1` as a substring.

**Example**
```
s1 = "ab", s2 = "eidbaooo" → true ("ba"),   s1 = "ab", s2 = "eidboaoo" → false
```

**Constraints**
* `1 <= s1.length, s2.length <= 10^4`; lowercase letters.

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-fixed-window-with-counts](v1-fixed-window-with-counts/README.md) | Fixed window with counts | `O(n)` | `O(1)` | [▶ animation](v1-fixed-window-with-counts/animation/index.html) |
