# 49. Group Anagrams

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Hashmap &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/group-anagrams/)

## Problem

Group the strings in `strs` so that anagrams are together. Return the groups in any order.

**Example 1**
```
Input:  strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
```

**Example 2**
```
Input:  strs = [""]
Output: [[""]]
```

**Constraints**
* `1 <= strs.length <= 10^4`, `0 <= strs[i].length <= 100`; lowercase letters.

## Solutions

Each folder below is a separate, self-contained Gradle project, ordered from the simplest idea to the most efficient one.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-sorted-word-key](v1-sorted-word-key/README.md) | Sorted-word key | `O(n·k log k)` | `O(n·k)` | [▶ animation](v1-sorted-word-key/animation/index.html) |
| [v2-letter-count-key](v2-letter-count-key/README.md) | Letter-count key | `O(n·k)` | `O(n·k)` | [▶ animation](v2-letter-count-key/animation/index.html) |
