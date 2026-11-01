# 3. Longest Substring Without Repeating Characters

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Sliding Window &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/longest-substring-without-repeating-characters/)

## Problem

Given a string `s`, return the length of the longest **substring** (contiguous) that contains no repeated characters.

**Example 1**
```
Input:  s = "abcabcbb"
Output: 3   ("abc")
```

**Example 2**
```
Input:  s = "bbbbb"
Output: 1
```

**Example 3**
```
Input:  s = "pwwkew"
Output: 3   ("wke"; "pwke" is a subsequence, not a substring)
```

**Constraints**
* `0 <= s.length <= 5 * 10^4`; letters, digits, symbols and spaces.

## Solutions

Each folder below is a separate, self-contained Gradle project, ordered from the simplest idea to the most efficient one.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-window-with-a-hash-set](v1-window-with-a-hash-set/README.md) | Window with a hash set | `O(n)` | `O(k)` | [▶ animation](v1-window-with-a-hash-set/animation/index.html) |
| [v2-window-with-last-seen-index](v2-window-with-last-seen-index/README.md) | Window with last-seen index | `O(n)` | `O(k)` | [▶ animation](v2-window-with-last-seen-index/animation/index.html) |
