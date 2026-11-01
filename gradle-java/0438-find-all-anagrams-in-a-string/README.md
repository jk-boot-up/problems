# 438. Find All Anagrams in a String

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Sliding Window &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/find-all-anagrams-in-a-string/)

## Problem

Return the start indices of all substrings of `s` that are anagrams of `p`, in any order.

**Example**
```
s = "cbaebabacd", p = "abc" → [0,6]
s = "abab", p = "ab"        → [0,1,2]
```

**Constraints**
* `1 <= s.length, p.length <= 3 * 10^4`; lowercase letters.

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-fixed-sliding-window-with-counts](v1-fixed-sliding-window-with-counts/README.md) | Fixed sliding window with counts | `O(n)` | `O(1)` | [▶ animation](v1-fixed-sliding-window-with-counts/animation/index.html) |
