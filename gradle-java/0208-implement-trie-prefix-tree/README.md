# 208. Implement Trie (Prefix Tree)

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Trie &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/implement-trie-prefix-tree/)

## Problem

Implement a **trie** (prefix tree) of lowercase words:
* `insert(word)`
* `search(word)`: `true` if `word` was inserted
* `startsWith(prefix)`: `true` if some inserted word starts with `prefix`

**Example**
```
insert("apple"); search("apple") → true; search("app") → false;
startsWith("app") → true; insert("app"); search("app") → true
```

**Constraints**
* `1 <= word.length, prefix.length <= 2000`; at most `3 * 10^4` calls.

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-array-of-children-trie](v1-array-of-children-trie/README.md) | Array-of-children trie | `O(L)` | `O(total letters)` | [▶ animation](v1-array-of-children-trie/animation/index.html) |
