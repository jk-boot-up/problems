# 127. Word Ladder — v2: Bidirectional BFS

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

## Approach: Bidirectional BFS

> Search outward from both ends at once; the frontiers meet in the middle after far fewer expansions.

**Bidirectional BFS.** Keep two frontier sets, from the start and from the end, in `MyHashSet`s. Always expand the **smaller**
frontier by trying every one-letter change; if a change lands in the other frontier, the ladders meet. Expanding the smaller side
keeps the number of generated words low.

* Time: **O(N·L·26)** — each word is expanded at most once, trying 26 letters at each of L positions.
* Space: **O(N)** — the word set and the frontiers.

Hash lookups use `MyHashMap` / `MyHashSet`, our own hash table (bucket array, chaining, resizing), instead of `java.util.HashMap`.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0127/v2/WordLadder.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0127/v2/WordLadderTest.java` | JUnit 6 tests |
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

* [v1-one-directional-bfs](../v1-one-directional-bfs/README.md): One-directional BFS (`O(N·L·26)` time, `O(N)` space)
