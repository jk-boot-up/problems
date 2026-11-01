# 145. Binary Tree Postorder Traversal — v1: Reversed modified preorder

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Binary Tree General &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/binary-tree-postorder-traversal/)

## Problem

Return the **postorder** traversal (left, right, node) of a binary tree's values.

**Example**
```
[1,null,2,3] → [3,2,1]
```

**Constraints**
* `0 <= n <= 100`

## Approach: Reversed modified preorder

> Postorder (left, right, node) is the reverse of a node, right, left traversal, which is easy with a stack.

**Reverse trick.** Traverse node, right, left with a stack (push the left child before the right), adding each value to the **front**
of the output list. The result is left, right, node.

* Time: **O(n)** — each node once.
* Space: **O(h)** — the stack (plus the output).

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0145/v1/PostorderTraversal.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0145/v1/PostorderTraversalTest.java` | JUnit 6 tests |
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
