# 236. Lowest Common Ancestor of a Binary Tree — v2: Recursive search

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Binary Tree General &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/)

## Problem

Given a binary tree and two of its nodes `p` and `q`, return their **lowest common ancestor**: the deepest node that has both `p`
and `q` as descendants (a node counts as a descendant of itself).

**Example 1**
```
Input:  root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
```

**Example 2**
```
Input:  same tree, p = 5, q = 4
Output: 5
```

**Constraints**
* `2 <= n <= 10^5`; values are unique; `p != q`; both exist in the tree.

## Approach: Recursive search

> A node is the LCA when p and q are found in different subtrees, or the node is one of them and the other is below.

**Bubble up what you find.** `lca(n)` returns `n` if `n` is null, `p` or `q`. Otherwise recurse into both children: if both return a
node, `n` is the split point, so return `n`. Otherwise return whichever side found something.

* Time: **O(n)** — each node is visited at most once.
* Space: **O(h)** — the recursion stack.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0236/v2/LowestCommonAncestor.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0236/v2/LowestCommonAncestorTest.java` | JUnit 6 tests |
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

* [v1-parent-map-and-ancestor-set](../v1-parent-map-and-ancestor-set/README.md): Parent map and ancestor set (`O(n)` time, `O(n)` space)
