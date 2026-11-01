# 199. Binary Tree Right Side View — v1: Right-first DFS

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

## Approach: Right-first DFS

> Visit right children before left; the first node reached at each depth is visible.

**DFS, right child first.** When `depth == out.size()`, this is the first node seen at that depth, and right-first order makes
it the rightmost.

* Time: **O(n)** — each node is visited once.
* Space: **O(h)** — the recursion stack.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0199/v1/RightSideView.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0199/v1/RightSideViewTest.java` | JUnit 6 tests |
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

* [v2-level-order-bfs](../v2-level-order-bfs/README.md): Level-order BFS (`O(n)` time, `O(w)` space)
