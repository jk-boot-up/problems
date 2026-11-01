# 106. Construct Binary Tree from Inorder and Postorder Traversal — v1: Hash map, walk postorder backwards

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Binary Tree General &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/)

## Problem

Given the `inorder` and `postorder` traversals of a binary tree with **unique** values, build and return the tree.

**Example 1**
```
Input:  inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
Output: [3,9,20,null,null,15,7]
```

**Example 2**
```
Input:  inorder = [-1], postorder = [-1]
Output: [-1]
```

**Constraints**
* `1 <= n <= 3000`; values are unique.

## Approach: Hash map, walk postorder backwards

> Postorder's last value is the root; build the right subtree first while walking postorder backwards.

**Mirror of the preorder version.** Read postorder from the end: each value is the root of the current inorder range. Split at its
inorder index (from a `MyHashMap`), and build the **right** subtree before the left, because postorder read backwards visits
root, right, left.

* Time: **O(n)** — one map lookup per node.
* Space: **O(n)** — the map and the recursion stack.

Hash lookups use `MyHashMap` / `MyHashSet`, our own hash table (bucket array, chaining, resizing), instead of `java.util.HashMap`.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0106/v1/BuildTreeInPost.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0106/v1/BuildTreeInPostTest.java` | JUnit 6 tests |
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
