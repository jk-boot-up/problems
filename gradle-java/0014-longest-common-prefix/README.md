# 14. Longest Common Prefix

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Array / String &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/longest-common-prefix/)

## Problem

Return the longest common prefix shared by all strings in `strs`, or `""` if there is none.

**Example 1**
```
Input:  strs = ["flower","flow","flight"]
Output: "fl"
```

**Example 2**
```
Input:  strs = ["dog","racecar","car"]
Output: ""
```

**Constraints**
* `1 <= strs.length <= 200`
* `0 <= strs[i].length <= 200`, lowercase English letters

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-vertical-scan](v1-vertical-scan/README.md) | Vertical scan | `O(S)` | `O(1)` | [▶ animation](v1-vertical-scan/animation/index.html) |
