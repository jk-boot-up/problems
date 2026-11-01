# 140. Word Break II

**Difficulty:** Hard &nbsp;|&nbsp; **Topic:** Backtracking &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/word-break-ii/)

## Problem

Return every way to split `s` into a space-separated sentence of dictionary words (words may be reused), in any order.

**Example**
```
s = "catsanddog", wordDict = ["cat","cats","and","sand","dog"] → ["cats and dog","cat sand dog"]
s = "catsandog", same dict → []
```

**Constraints**
* `1 <= s.length <= 20`

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-memoized-backtracking](v1-memoized-backtracking/README.md) | Memoized backtracking | `O(2ⁿ)` | `O(2ⁿ)` | [▶ animation](v1-memoized-backtracking/animation/index.html) |
