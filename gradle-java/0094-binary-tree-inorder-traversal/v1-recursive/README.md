# 94. Binary Tree Inorder Traversal — v1: Recursive

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Binary Tree General &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/binary-tree-inorder-traversal/)

## Problem

Return the **inorder** traversal (left, node, right) of a binary tree's values.

**Example**
```
[1,null,2,3] → [1,3,2]
```

**Constraints**
* `0 <= n <= 100`

**Follow-up:** iteratively.

## Approach: Recursive

> inorder(left), visit, inorder(right).

**Recursion.** The call stack plays the role of the explicit stack.

* Time: **O(n)** — one call per node.
* Space: **O(h)** — the recursion depth.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0094/v1/InorderTraversal.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0094/v1/InorderTraversalTest.java` | JUnit 6 tests |
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

* [v2-iterative-with-a-stack](../v2-iterative-with-a-stack/README.md): Iterative with a stack (`O(n)` time, `O(h)` space)
