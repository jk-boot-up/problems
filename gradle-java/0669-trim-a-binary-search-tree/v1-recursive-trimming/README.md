# 669. Trim a Binary Search Tree — v1: Recursive trimming

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Binary Search Tree &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/trim-a-binary-search-tree/)

## Problem

Remove every node whose value lies outside `[low, high]` from a BST, keeping the relative structure of the remaining nodes. Return the new root.

**Example**
```
root = [1,0,2], low = 1, high = 2           → [1,null,2]
root = [3,0,4,null,2,null,null,1], low = 1, high = 3 → [3,2,null,1]
```

**Constraints**
* `1 <= n <= 10^4`

## Approach: Recursive trimming

> A node below low can only keep its right subtree; above high, only its left subtree.

**Recursion.** If `node.val < low`, its whole left subtree is too small: return `trim(node.right)`. If `node.val > high`, return
`trim(node.left)`. Otherwise trim both children and keep the node.

* Time: **O(n)** — each node once.
* Space: **O(h)** — the recursion stack.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0669/v1/TrimBST.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0669/v1/TrimBSTTest.java` | JUnit 6 tests |
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
