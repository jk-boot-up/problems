# 199. Binary Tree Right Side View — v2: Level-order BFS

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Binary Tree BFS &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/binary-tree-right-side-view/)

## Problem

Imagine standing on the right side of a binary tree. Return the values you can see, from top to bottom.

**Example 1**
```
Input:  [1,2,3,null,5,null,4]
Output: [1,3,4]
```

**Example 2**
```
Input:  [1,2,3,4,null,null,null,5]
Output: [1,3,4,5]
```

**Constraints**
* `0 <= n <= 100`

## Approach: Level-order BFS

> Standing on the right, you see the last node of every level.

**BFS by levels.** Process the queue one level at a time; the last node popped in each level is visible.

* Time: **O(n)** — each node is enqueued once.
* Space: **O(w)** — the widest level.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0199/v2/RightSideView.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0199/v2/RightSideViewTest.java` | JUnit 6 tests |
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

* [v1-right-first-dfs](../v1-right-first-dfs/README.md): Right-first DFS (`O(n)` time, `O(h)` space)
