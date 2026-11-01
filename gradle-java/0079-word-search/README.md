# 79. Word Search

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Backtracking &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/word-search/)

## Problem

Given an `m × n` grid of letters and a `word`, return `true` if the word can be traced through **adjacent** cells (horizontally or
vertically), using each cell at most once.

**Example**
```
Input:  board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
        word = "ABCCED" → true,  "SEE" → true,  "ABCB" → false
```

**Constraints**
* `1 <= m, n <= 6`; `1 <= word.length <= 15`

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-dfs-backtracking](v1-dfs-backtracking/README.md) | DFS backtracking | `O(m·n·3^L)` | `O(L)` | [▶ animation](v1-dfs-backtracking/animation/index.html) |
