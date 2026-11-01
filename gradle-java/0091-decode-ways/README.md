# 91. Decode Ways

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** 1D DP &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/decode-ways/)

## Problem

Letters map to numbers `A=1 … Z=26`. Given a digit string `s`, return how many ways it can be decoded. `"06"` is not valid (no leading zeros).

**Example**
```
"12" → 2 ("AB", "L"),   "226" → 3,   "06" → 0
```

**Constraints**
* `1 <= s.length <= 100`; digits only.

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-two-rolling-variables](v1-two-rolling-variables/README.md) | Two rolling variables | `O(n)` | `O(1)` | [▶ animation](v1-two-rolling-variables/animation/index.html) |
