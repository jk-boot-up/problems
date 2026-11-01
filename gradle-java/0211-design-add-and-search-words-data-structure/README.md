# 211. Design Add and Search Words Data Structure

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Trie &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/design-add-and-search-words-data-structure/)

## Problem

Design `WordDictionary`:
* `addWord(word)`: add a lowercase word;
* `search(word)`: `true` if any added word matches, where `.` matches **any one letter**.

**Example**
```
addWord("bad"); addWord("dad"); addWord("mad");
search("pad") → false; search("bad") → true; search(".ad") → true; search("b..") → true
```

**Constraints**
* `1 <= word.length <= 25`; at most 2 dots per search; at most `10^4` calls.

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-trie-with-wildcard-dfs](v1-trie-with-wildcard-dfs/README.md) | Trie with wildcard DFS | `O(L)` | `O(total letters)` | [▶ animation](v1-trie-with-wildcard-dfs/animation/index.html) |
