# 662. Maximum Width of Binary Tree — v1: BFS with position indices

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Binary Tree BFS &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/maximum-width-of-binary-tree/)

## Problem

The width of a level is the number of positions between its leftmost and rightmost non-null nodes, counting the null positions in between
as they would appear in a complete tree. Return the maximum width over all levels (it fits in 32 bits).

**Example**
```
[1,3,2,5,3,null,9]               → 4
[1,3,2,5,null,null,9,6,null,7]   → 7
```

**Constraints**
* `1 <= n <= 3000`

## Approach: BFS with position indices

> Number nodes like a heap (left = 2i, right = 2i + 1); a level's width is last index − first index + 1.

**Positions.** BFS with each node's position: children of `p` are `2p` and `2p + 1`. To avoid huge numbers, renumber each level relative to its
first position before expanding. Width = last − first + 1.

* Time: **O(n)** — each node once.
* Space: **O(w)** — the widest level.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0662/v1/MaximumWidth.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0662/v1/MaximumWidthTest.java` | JUnit 6 tests |
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
* **Complexity:** time and space cost, plotted against the common growth curves.

Switch between Light, Medium and Dark themes in the header.
