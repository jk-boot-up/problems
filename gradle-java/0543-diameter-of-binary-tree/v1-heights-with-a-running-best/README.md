# 543. Diameter of Binary Tree — v1: Heights with a running best

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Binary Tree General &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/diameter-of-binary-tree/)

## Problem

Return the **diameter** of a binary tree: the number of edges on the longest path between any two nodes (it need not pass through the root).

**Example**
```
[1,2,3,4,5] → 3   (4 → 2 → 1 → 3 or 5 → 2 → 1 → 3)
```

**Constraints**
* `1 <= n <= 10^4`

## Approach: Heights with a running best

> The longest path through a node is its left height plus its right height; track the maximum while computing heights.

**Post-order heights.** `height(n) = 1 + max(height(left), height(right))`. At each node, `left + right` edges form the longest path
bending there; keep the maximum.

* Time: **O(n)** — each node once.
* Space: **O(h)** — the recursion stack.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0543/v1/DiameterOfBinaryTree.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0543/v1/DiameterOfBinaryTreeTest.java` | JUnit 6 tests |
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
