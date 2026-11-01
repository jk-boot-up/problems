# 127. Word Ladder — v1: One-directional BFS

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

## Approach: One-directional BFS

> BFS from the begin word, one level per transformation, until the end word appears.

**Plain BFS.** Level by level, generate every one-letter change of every word in the queue; keep those in the word set (removing
them to mark as visited).

* Time: **O(N·L·26)** — each word is dequeued once.
* Space: **O(N)** — the word set and the queue.

Hash lookups use `MyHashMap` / `MyHashSet`, our own hash table (bucket array, chaining, resizing), instead of `java.util.HashMap`.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0127/v1/WordLadder.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0127/v1/WordLadderTest.java` | JUnit 6 tests |
| `animation/index.html` | Animated walkthrough with spoken narration |

## Build and test

This folder is a standalone Gradle 9.8.2 project. Only a JDK is needed to start Gradle; JDK 25 is downloaded
automatically if it is missing.

```bash
./gradlew test
```

## Animation

Open [`animation/index.html`](animation/index.html) in a browser. It has three tabs:

* **Problem:** the statement and the key idea.
* **Walkthrough:** pick a scenario and press **Play**. Each step is animated and read aloud by your browser's speech
  engine (use the 🔊 *Narration* button to turn the voice on or off; a female voice, Amy when installed, is preferred). Keys: space = play/pause, ← / → = step, 1–9 = scenario.
* **Complexity:** time and space cost, plotted against the common growth curves, and compared with the other approaches.

Switch between Light, Medium and Dark themes in the header.

## Other approaches

* [v2-bidirectional-bfs](../v2-bidirectional-bfs/README.md): Bidirectional BFS (`O(N·L·26)` time, `O(N)` space)
