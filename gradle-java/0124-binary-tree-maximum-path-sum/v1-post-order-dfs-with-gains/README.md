# 124. Binary Tree Maximum Path Sum — v1: Post-order DFS with gains

**Difficulty:** Hard &nbsp;|&nbsp; **Topic:** Binary Tree General &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/binary-tree-maximum-path-sum/)

## Problem

A **path** is a sequence of nodes connected by edges, each node used at most once; it need not pass through the root. Return the
maximum sum of node values over all non-empty paths.

**Example 1**
```
Input:  [1,2,3]
Output: 6   (2 → 1 → 3)
```

**Example 2**
```
Input:  [-10,9,20,null,null,15,7]
Output: 42   (15 → 20 → 7)
```

**Constraints**
* `1 <= n <= 3 * 10^4`; `-1000 <= Node.val <= 1000`

## Approach: Post-order DFS with gains

> Each node reports its best downward branch; the best path through it is the node plus both non-negative branches.

**Gain per node.** `gain(n)` = the best sum of a path that starts at `n` and goes down one side: `n.val + max(0, gain(left), gain(right))`.
While computing it, the best path that **bends** at `n` is `n.val + max(0, gain(left)) + max(0, gain(right))`; keep the maximum
over all nodes. Negative branches are dropped (max with 0).

* Time: **O(n)** — each node is visited once.
* Space: **O(h)** — the recursion stack.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0124/v1/MaximumPathSum.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0124/v1/MaximumPathSumTest.java` | JUnit 6 tests |
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
