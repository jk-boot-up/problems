# 783. Minimum Distance Between BST Nodes — v1: In-order with previous value

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Binary Search Tree &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/minimum-distance-between-bst-nodes/)

## Problem

Return the minimum difference between the values of any two different nodes of a BST.

**Example**
```
[4,2,6,1,3] → 1,   [1,0,48,null,null,12,49] → 1
```

**Constraints**
* `2 <= n <= 100`

## Approach: In-order with previous value

> In-order traversal visits BST values in sorted order; the minimum gap is between neighbours.

**Sorted neighbours.** Iterative in-order traversal; compare each value with the previous one.

* Time: **O(n)** — each node once.
* Space: **O(h)** — the stack.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0783/v1/MinimumDistanceBST.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0783/v1/MinimumDistanceBSTTest.java` | JUnit 6 tests |
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
