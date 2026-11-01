# 235. Lowest Common Ancestor of a Binary Search Tree — v1: Walk down by value

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Binary Search Tree &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/)

## Problem

Given a BST and two of its nodes `p` and `q`, return their lowest common ancestor (a node is a descendant of itself).

**Example**
```
root = [6,2,8,0,4,7,9,null,null,3,5]: p = 2, q = 8 → 6;  p = 2, q = 4 → 2
```

**Constraints**
* `2 <= n <= 10^5`; values are unique; `p` and `q` exist.

## Approach: Walk down by value

> In a BST, walk down from the root: go left if both values are smaller, right if both are larger; otherwise you are at the split.

**Use the ordering.** If both values are below the current node, the LCA is in the left subtree; if both are above, in the right. Otherwise
the current node separates them (or equals one of them): it is the LCA.

* Time: **O(h)** — one root-to-node walk.
* Space: **O(1)** — iterative.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0235/v1/LowestCommonAncestorBST.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0235/v1/LowestCommonAncestorBSTTest.java` | JUnit 6 tests |
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
