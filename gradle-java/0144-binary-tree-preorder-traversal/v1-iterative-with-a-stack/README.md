# 144. Binary Tree Preorder Traversal — v1: Iterative with a stack

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Binary Tree General &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/binary-tree-preorder-traversal/)

## Problem

Return the **preorder** traversal (node, left, right) of a binary tree's values.

**Example**
```
[1,null,2,3] → [1,2,3]
```

**Constraints**
* `0 <= n <= 100`

## Approach: Iterative with a stack

> Visit a node, then its left subtree, then its right; with a stack, push the right child first so the left pops first.

**Stack.** Pop a node, record it, push its right child then its left child.

* Time: **O(n)** — each node once.
* Space: **O(h)** — the stack.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0144/v1/PreorderTraversal.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0144/v1/PreorderTraversalTest.java` | JUnit 6 tests |
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
