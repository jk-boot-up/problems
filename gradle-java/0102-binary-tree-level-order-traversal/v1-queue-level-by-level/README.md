# 102. Binary Tree Level Order Traversal — v1: Queue, level by level

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Binary Tree BFS &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/binary-tree-level-order-traversal/)

## Problem

Return the level-order traversal of a binary tree's values: left to right, level by level, as a list of lists.

**Example**
```
Input:  [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]
```

**Constraints**
* `0 <= n <= 2000`

## Approach: Queue, level by level

> A queue visits nodes in level order; cut it into levels by processing exactly the current queue size each round.

**BFS.** Each round, remember `size = queue.size()`; pop exactly `size` nodes into one list and enqueue their children.

* Time: **O(n)** — each node is enqueued once.
* Space: **O(w)** — the widest level (plus the output).

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0102/v1/LevelOrderTraversal.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0102/v1/LevelOrderTraversalTest.java` | JUnit 6 tests |
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
