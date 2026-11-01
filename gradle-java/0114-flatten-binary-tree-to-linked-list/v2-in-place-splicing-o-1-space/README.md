# 114. Flatten Binary Tree to Linked List — v2: In-place splicing (O(1) space)

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Binary Tree General &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/flatten-binary-tree-to-linked-list/)

## Problem

Flatten a binary tree **in place** into a "linked list" that uses the `right` pointers, with every `left` set to `null`, in
**preorder** order.

**Example**
```
Input:  [1,2,5,3,4,null,6]
Output: [1,null,2,null,3,null,4,null,5,null,6]
```

**Constraints**
* `0 <= n <= 2000`

**Follow-up:** O(1) extra space.

## Approach: In-place splicing (O(1) space)

> For each node with a left child, splice the left subtree between the node and its right subtree.

**Splice like Morris traversal.** For the current node with a left child, find the rightmost node of the left subtree (the last
node of the left part in preorder). Attach the current right subtree there, move the left subtree to the right, and clear `left`.
Advance to `right`.

* Time: **O(n)** — each edge is walked a constant number of times.
* Space: **O(1)** — no stack or list.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0114/v2/FlattenTree.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0114/v2/FlattenTreeTest.java` | JUnit 6 tests |
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

* [v1-preorder-list-then-relink](../v1-preorder-list-then-relink/README.md): Preorder list, then relink (`O(n)` time, `O(n)` space)
