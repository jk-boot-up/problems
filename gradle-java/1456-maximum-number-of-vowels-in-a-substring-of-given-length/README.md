# 1456. Maximum Number of Vowels in a Substring of Given Length

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Sliding Window &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/)

## Problem

Return the maximum number of vowels in any substring of `s` with length `k`.

**Example**
```
s = "abciiidef", k = 3 → 3,   s = "aeiou", k = 2 → 2,   s = "leetcode", k = 3 → 2
```

**Constraints**
* `1 <= k <= s.length <= 10^5`

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-fixed-sliding-window](v1-fixed-sliding-window/README.md) | Fixed sliding window | `O(n)` | `O(1)` | [▶ animation](v1-fixed-sliding-window/animation/index.html) |
