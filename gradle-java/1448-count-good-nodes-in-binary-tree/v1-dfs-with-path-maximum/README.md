# 1448. Count Good Nodes in Binary Tree — v1: DFS with path maximum

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Binary Tree General &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/count-good-nodes-in-binary-tree/)

## Problem

A node is **good** if no node on the path from the root to it has a greater value. Return the number of good nodes.

**Example**
```
[3,1,4,3,null,1,5] → 4,   [3,3,null,4,2] → 3,   [1] → 1
```

**Constraints**
* `1 <= n <= 10^5`

## Approach: DFS with path maximum

> Carry the largest value seen on the path from the root; a node is good if it is at least that large.

**Path maximum.** `dfs(node, maxSoFar)`: count the node if `node.val >= maxSoFar`, then recurse with `max(maxSoFar, node.val)`.

* Time: **O(n)** — each node once.
* Space: **O(h)** — the recursion stack.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p1448/v1/CountGoodNodes.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p1448/v1/CountGoodNodesTest.java` | JUnit 6 tests |
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
