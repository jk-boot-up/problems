# 226. Invert Binary Tree — v2: Recursive swap

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Binary Tree General &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/invert-binary-tree/)

## Problem

Invert a binary tree (mirror it left-to-right) and return its root.

**Example 1**
```
Input:  [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]
```

**Example 2**
```
Input:  [2,1,3]
Output: [2,3,1]
```

**Constraints**
* `0 <= n <= 100`; `-100 <= Node.val <= 100`

## Approach: Recursive swap

> Swap every node's left and right children; the whole tree becomes its mirror image.

**Recursion.** Invert both subtrees, then swap them.

* Time: **O(n)** — each node is visited once.
* Space: **O(h)** — the recursion stack.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0226/v2/InvertBinaryTree.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0226/v2/InvertBinaryTreeTest.java` | JUnit 6 tests |
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

* [v1-iterative-bfs](../v1-iterative-bfs/README.md): Iterative BFS (`O(n)` time, `O(w)` space)
