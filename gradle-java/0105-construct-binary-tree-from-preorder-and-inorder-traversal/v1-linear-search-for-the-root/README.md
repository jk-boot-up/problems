# 105. Construct Binary Tree from Preorder and Inorder Traversal — v1: Linear search for the root

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

## Approach: Linear search for the root

> Same divide-and-conquer, but scan the inorder range to find each root.

**No map.** Find the root's inorder position by scanning `inorder[lo..hi]`.

* Time: **O(n²)** — a skewed tree makes each scan linear.
* Space: **O(h)** — the recursion stack.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0105/v1/BuildTreePreIn.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0105/v1/BuildTreePreInTest.java` | JUnit 6 tests |
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

* [v2-hash-map-of-inorder-positions](../v2-hash-map-of-inorder-positions/README.md): Hash map of inorder positions (`O(n)` time, `O(n)` space)
