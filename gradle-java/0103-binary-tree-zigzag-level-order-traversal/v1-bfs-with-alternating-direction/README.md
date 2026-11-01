# 103. Binary Tree Zigzag Level Order Traversal — v1: BFS with alternating direction

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Binary Tree BFS &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/)

## Problem

Return the zigzag level-order traversal: the first level left to right, the next right to left, and so on.

**Example**
```
Input:  [3,9,20,null,null,15,7]
Output: [[3],[20,9],[15,7]]
```

**Constraints**
* `0 <= n <= 2000`

## Approach: BFS with alternating direction

> Do a normal level-order traversal, but fill every other level from the right.

**BFS + deque per level.** Process levels as usual. For left-to-right levels append values at the back; for right-to-left levels
add them at the front. Flip the direction after each level.

* Time: **O(n)** — each node is processed once.
* Space: **O(w)** — the widest level.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0103/v1/ZigzagLevelOrder.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0103/v1/ZigzagLevelOrderTest.java` | JUnit 6 tests |
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
