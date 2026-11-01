# 114. Flatten Binary Tree to Linked List — v1: Preorder list, then relink

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

## Approach: Preorder list, then relink

> Record the nodes in preorder, then link each to the next.

**Collect and relink.** A preorder traversal fills a list; then `list[i].left = null`, `list[i].right = list[i+1]`.

* Time: **O(n)** — one traversal and one relinking pass.
* Space: **O(n)** — the list of nodes.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0114/v1/FlattenTree.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0114/v1/FlattenTreeTest.java` | JUnit 6 tests |
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

* [v2-in-place-splicing-o-1-space](../v2-in-place-splicing-o-1-space/README.md): In-place splicing (O(1) space) (`O(n)` time, `O(1)` space)
