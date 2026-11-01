# 76. Minimum Window Substring

**Difficulty:** Hard &nbsp;|&nbsp; **Topic:** Sliding Window &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/minimum-window-substring/)

## Problem

Given strings `s` and `t`, return the **shortest substring** of `s` that contains every character of `t` (including duplicates).
Return `""` if there is none. The answer is unique when it exists.

**Example 1**
```
Input:  s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
```

**Example 2**
```
Input:  s = "a", t = "a"
Output: "a"
```

**Example 3**
```
Input:  s = "a", t = "aa"
Output: ""
```

**Constraints**
* `1 <= s.length, t.length <= 10^5`; upper- and lower-case letters.

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-sliding-window-with-counts](v1-sliding-window-with-counts/README.md) | Sliding window with counts | `O(m + n)` | `O(1)` | [▶ animation](v1-sliding-window-with-counts/animation/index.html) |
