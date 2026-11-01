# 212. Word Search II

**Difficulty:** Hard &nbsp;|&nbsp; **Topic:** Trie &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/word-search-ii/)

## Problem

Given an `m × n` board of letters and a list of `words`, return all words that can be formed by a path of **adjacent** cells
(horizontally or vertically). A cell may be used at most once per word. Return the words in any order.

**Example**
```
Input:  board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]
        words = ["oath","pea","eat","rain"]
Output: ["eat","oath"]
```

**Constraints**
* `1 <= m, n <= 12`; `1 <= words.length <= 3 * 10^4`; `1 <= words[i].length <= 10`

## Solutions

Each folder below is a separate, self-contained Gradle project, ordered from the simplest idea to the most efficient one.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-separate-dfs-for-every-word](v1-separate-dfs-for-every-word/README.md) | Separate DFS for every word | `O(W·m·n·3^L)` | `O(L)` | [▶ animation](v1-separate-dfs-for-every-word/animation/index.html) |
| [v2-trie-backtracking](v2-trie-backtracking/README.md) | Trie + backtracking | `O(m·n·3^L)` | `O(total letters)` | [▶ animation](v2-trie-backtracking/animation/index.html) |
