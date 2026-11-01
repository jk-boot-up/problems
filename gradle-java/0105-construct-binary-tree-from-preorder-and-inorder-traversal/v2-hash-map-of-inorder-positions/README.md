# 105. Construct Binary Tree from Preorder and Inorder Traversal — v2: Hash map of inorder positions

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Binary Tree General &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/)

## Problem

Given the `preorder` and `inorder` traversals of a binary tree with **unique** values, build and return the tree.

**Example 1**
```
Input:  preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]
```

**Example 2**
```
Input:  preorder = [-1], inorder = [-1]
Output: [-1]
```

**Constraints**
* `1 <= n <= 3000`; values are unique.

## Approach: Hash map of inorder positions

> Preorder's first value is the root; its position in inorder splits the left and right subtrees.

**Divide by the root.** The next unused preorder value is the root of the current inorder range `[lo, hi]`. Its inorder index `m`
splits the range: `[lo, m-1]` is the left subtree, `[m+1, hi]` the right. Build left first, because preorder lists the left subtree
before the right. A `MyHashMap` from value to inorder index makes each split O(1).

* Time: **O(n)** — one map lookup per node.
* Space: **O(n)** — the map and the recursion stack.

Hash lookups use `MyHashMap` / `MyHashSet`, our own hash table (bucket array, chaining, resizing), instead of `java.util.HashMap`.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0105/v2/BuildTreePreIn.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0105/v2/BuildTreePreInTest.java` | JUnit 6 tests |
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

* [v1-linear-search-for-the-root](../v1-linear-search-for-the-root/README.md): Linear search for the root (`O(n²)` time, `O(h)` space)
