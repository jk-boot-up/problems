# 111. Minimum Depth of Binary Tree — v1: BFS to the first leaf

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Binary Tree BFS &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/minimum-depth-of-binary-tree/)

## Problem

Return the **minimum depth** of a binary tree: the number of nodes on the shortest path from the root down to a **leaf** (a node with no
children).

**Example**
```
[3,9,20,null,null,15,7]          → 2
[2,null,3,null,4,null,5,null,6]  → 5
```

**Constraints**
* `0 <= n <= 10^5`

## Approach: BFS to the first leaf

> Breadth-first search stops at the first leaf it meets: that leaf is on the shallowest level.

**Level-order search.** Process the tree level by level; the first leaf found ends the search, so deeper levels are never visited.
(A plain `min(left, right)` recursion is wrong when one child is missing.)

* Time: **O(n)** — in the worst case all nodes are visited, but usually far fewer.
* Space: **O(w)** — the widest level in the queue.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0111/v1/MinimumDepth.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0111/v1/MinimumDepthTest.java` | JUnit 6 tests |
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
