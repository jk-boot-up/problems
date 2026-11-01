# 139. Word Break

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** 1D DP &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/word-break/)

## Problem

Return `true` if `s` can be split into a sequence of one or more words from `wordDict` (words may be reused).

**Example**
```
s = "leetcode", wordDict = ["leet","code"]            → true
s = "applepenapple", wordDict = ["apple","pen"]       → true
s = "catsandog", wordDict = ["cats","dog","sand","and","cat"] → false
```

**Constraints**
* `1 <= s.length <= 300`; `1 <= wordDict.length <= 1000`; `1 <= wordDict[i].length <= 20`

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-dp-over-prefixes](v1-dp-over-prefixes/README.md) | DP over prefixes | `O(n · L²)` | `O(n + D)` | [▶ animation](v1-dp-over-prefixes/animation/index.html) |
