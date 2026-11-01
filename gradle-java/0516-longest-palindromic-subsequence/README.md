# 516. Longest Palindromic Subsequence

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Multidimensional DP &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/longest-palindromic-subsequence/)

## Problem

Return the length of the longest **palindromic subsequence** of `s`.

**Example**
```
"bbbab" → 4 ("bbbb"),   "cbbd" → 2 ("bb")
```

**Constraints**
* `1 <= s.length <= 1000`

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-interval-dp](v1-interval-dp/README.md) | Interval DP | `O(n²)` | `O(n²)` | [▶ animation](v1-interval-dp/animation/index.html) |
