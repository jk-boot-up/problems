# 222. Count Complete Tree Nodes — v2: Perfect-subtree shortcut

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Binary Tree General &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/count-complete-tree-nodes/)

## Problem

Count the nodes of a **complete** binary tree: every level is full except possibly the last, which is filled from the left.

**Example 1**
```
Input:  [1,2,3,4,5,6]
Output: 6
```

**Example 2**
```
Input:  []
Output: 0
```

**Constraints**
* `0 <= n <= 5 * 10^4`; the tree is complete.

**Follow-up:** faster than O(n).

## Approach: Perfect-subtree shortcut

> If the leftmost and rightmost depths match, the subtree is perfect (2^h − 1 nodes); otherwise recurse.

**Compare edge heights.** Walk down the left edge and the right edge. If both heights are `h`, the subtree is perfect and has
`2^h - 1` nodes. Otherwise count `1 + count(left) + count(right)`; one of the two halves is always perfect, so only one branch goes deep.

* Time: **O(log² n)** — O(log n) levels of recursion, each measuring heights in O(log n).
* Space: **O(log n)** — the recursion depth.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0222/v2/CountCompleteTreeNodes.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0222/v2/CountCompleteTreeNodesTest.java` | JUnit 6 tests |
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

* [v1-count-every-node](../v1-count-every-node/README.md): Count every node (`O(n)` time, `O(log n)` space)
