# 236. Lowest Common Ancestor of a Binary Tree — v1: Parent map and ancestor set

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

## Approach: Parent map and ancestor set

> Record every node's parent, collect p's ancestors in a set, then climb from q until hitting one.

**Parent pointers.** Traverse once to fill a `MyHashMap<node, parent>`. Put all ancestors of `p` (including `p`) in a `MyHashSet`.
Climb from `q` until reaching a node in that set.

* Time: **O(n)** — one traversal plus two climbs.
* Space: **O(n)** — the parent map.

Hash lookups use `MyHashMap` / `MyHashSet`, our own hash table (bucket array, chaining, resizing), instead of `java.util.HashMap`.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0236/v1/LowestCommonAncestor.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0236/v1/LowestCommonAncestorTest.java` | JUnit 6 tests |
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

* [v2-recursive-search](../v2-recursive-search/README.md): Recursive search (`O(n)` time, `O(h)` space)
