# 5. Longest Palindromic Substring

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Multidimensional DP &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/longest-palindromic-substring/)

## Problem

Return the longest **palindromic substring** of `s`.

**Example**
```
"babad" → "bab" (or "aba"),   "cbbd" → "bb"
```

**Constraints**
* `1 <= s.length <= 1000`; digits and English letters.

## Solutions

Each folder below is a separate, self-contained Gradle project, ordered from the simplest idea to the most efficient one.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-dp-table](v1-dp-table/README.md) | DP table | `O(n²)` | `O(n²)` | [▶ animation](v1-dp-table/animation/index.html) |
| [v2-expand-around-centre](v2-expand-around-centre/README.md) | Expand around centre | `O(n²)` | `O(1)` | [▶ animation](v2-expand-around-centre/animation/index.html) |
