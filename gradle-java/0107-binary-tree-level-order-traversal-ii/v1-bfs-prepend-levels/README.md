# 107. Binary Tree Level Order Traversal II — v1: BFS, prepend levels

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Binary Tree BFS &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/binary-tree-level-order-traversal-ii/)

## Problem

Return the level-order traversal from the **bottom** level up (each level left to right).

**Example**
```
[3,9,20,null,null,15,7] → [[15,7],[9,20],[3]]
```

**Constraints**
* `0 <= n <= 2000`

## Approach: BFS, prepend levels

> A normal level-order traversal, adding each level to the front of the result.

**BFS + addFirst.** Collect each level as usual and insert it at the front of a `LinkedList`.

* Time: **O(n)** — each node once.
* Space: **O(w)** — the widest level.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0107/v1/LevelOrderBottom.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0107/v1/LevelOrderBottomTest.java` | JUnit 6 tests |
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
