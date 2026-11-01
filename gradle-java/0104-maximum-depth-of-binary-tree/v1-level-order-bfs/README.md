# 104. Maximum Depth of Binary Tree — v1: Level-order BFS

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Binary Tree General &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/maximum-depth-of-binary-tree/)

## Problem

Return the **maximum depth** of a binary tree: the number of nodes on the longest path from the root down to a leaf.

**Example 1**
```
Input:  root = [3,9,20,null,null,15,7]
Output: 3
```

**Example 2**
```
Input:  root = [1,null,2]
Output: 2
```

**Constraints**
* `0 <= n <= 10^4`; `-100 <= Node.val <= 100`

## Approach: Level-order BFS

> Count how many levels a breadth-first traversal visits.

**Queue by levels.** Push the root; for each level, pop exactly the nodes currently in the queue and push their children. Count the levels.

* Time: **O(n)** — each node is enqueued once.
* Space: **O(w)** — w is the widest level (up to about n/2).

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0104/v1/MaximumDepth.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0104/v1/MaximumDepthTest.java` | JUnit 6 tests |
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

* [v2-recursive-dfs](../v2-recursive-dfs/README.md): Recursive DFS (`O(n)` time, `O(h)` space)
