# 94. Binary Tree Inorder Traversal — v2: Iterative with a stack

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

## Approach: Iterative with a stack

> Left subtree, node, right subtree; iteratively, a stack holds the path of nodes still waiting to be visited.

**Stack.** Push the left spine; pop a node, record it, move to its right child, and repeat.

* Time: **O(n)** — each node is pushed and popped once.
* Space: **O(h)** — the stack.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0094/v2/InorderTraversal.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0094/v2/InorderTraversalTest.java` | JUnit 6 tests |
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

* [v1-recursive](../v1-recursive/README.md): Recursive (`O(n)` time, `O(h)` space)
