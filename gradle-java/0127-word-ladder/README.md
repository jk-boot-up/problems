# 127. Word Ladder

**Difficulty:** Hard &nbsp;|&nbsp; **Topic:** Graph BFS &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/word-ladder/)

## Problem

A **transformation sequence** from `beginWord` to `endWord` changes one letter at a time, and every word after the first must be in
`wordList`. Return the number of words in the **shortest** such sequence, or `0` if none exists.

**Example 1**
```
Input:  beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
Output: 5   (hit → hot → dot → dog → cog)
```

**Example 2**
```
Input:  same, but without "cog"
Output: 0
```

**Constraints**
* `1 <= beginWord.length <= 10`; `1 <= wordList.length <= 5000`; lowercase letters.

## Solutions

Each folder below is a separate, self-contained Gradle project, ordered from the simplest idea to the most efficient one.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-one-directional-bfs](v1-one-directional-bfs/README.md) | One-directional BFS | `O(N·L·26)` | `O(N)` | [▶ animation](v1-one-directional-bfs/animation/index.html) |
| [v2-bidirectional-bfs](v2-bidirectional-bfs/README.md) | Bidirectional BFS | `O(N·L·26)` | `O(N)` | [▶ animation](v2-bidirectional-bfs/animation/index.html) |
