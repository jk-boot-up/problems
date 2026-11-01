# 424. Longest Repeating Character Replacement

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Sliding Window &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/longest-repeating-character-replacement/)

## Problem

You may change at most `k` characters of `s` (uppercase letters). Return the length of the longest substring containing a single
repeated letter after the changes.

**Example**
```
s = "ABAB", k = 2 → 4,   s = "AABABBA", k = 1 → 4
```

**Constraints**
* `1 <= s.length <= 10^5`; `0 <= k <= s.length`

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-sliding-window-with-max-count](v1-sliding-window-with-max-count/README.md) | Sliding window with max count | `O(n)` | `O(1)` | [▶ animation](v1-sliding-window-with-max-count/animation/index.html) |
