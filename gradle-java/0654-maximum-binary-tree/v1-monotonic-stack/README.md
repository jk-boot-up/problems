# 654. Maximum Binary Tree — v1: Monotonic stack

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Stack &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/maximum-binary-tree/)

## Problem

Build the **maximum binary tree** of distinct `nums`: the root is the maximum; its left subtree is built from the part before it and its right
subtree from the part after it, recursively.

**Example**
```
[3,2,1,6,0,5] → [6,3,5,null,2,0,null,null,1]
```

**Constraints**
* `1 <= nums.length <= 1000`; values are distinct.

## Approach: Monotonic stack

> A decreasing stack builds the tree in one pass: each new value adopts the smaller values it pops as its left subtree.

**Decreasing stack of nodes.** For each value create a node; pop every smaller node, the last one popped becoming its left child; if the
stack is not empty, the new node becomes the right child of the top. The bottom of the stack is the root.

* Time: **O(n)** — each node is pushed and popped once.
* Space: **O(n)** — the stack.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0654/v1/MaximumBinaryTree.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0654/v1/MaximumBinaryTreeTest.java` | JUnit 6 tests |
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
