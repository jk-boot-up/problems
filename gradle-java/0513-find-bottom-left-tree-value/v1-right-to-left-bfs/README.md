# 513. Find Bottom Left Tree Value — v1: Right-to-left BFS

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Binary Tree BFS &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/find-bottom-left-tree-value/)

## Problem

Return the leftmost value in the **last** row of a binary tree.

**Example**
```
[2,1,3]                          → 1
[1,2,3,4,null,5,6,null,null,7]   → 7
```

**Constraints**
* `1 <= n <= 10^4`

## Approach: Right-to-left BFS

> Do a BFS that visits each level right to left; the very last node dequeued is the bottom-left one.

**Reverse BFS.** Enqueue the right child before the left child. Then the last node dequeued is in the deepest level and is its leftmost
node.

* Time: **O(n)**.
* Space: **O(w)** — the widest level.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0513/v1/BottomLeftValue.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0513/v1/BottomLeftValueTest.java` | JUnit 6 tests |
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
