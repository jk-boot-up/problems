# 427. Construct Quad-Tree — v1: Recursive quadrants

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Divide & Conquer &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/construct-quad-tree/)

## Problem

Given an `n × n` grid of `0`s and `1`s (`n` a power of two), build its **quad tree**. Each node has `val`, `isLeaf` and four children
(`topLeft`, `topRight`, `bottomLeft`, `bottomRight`). A uniform region is a leaf whose `val` is that value; any other region is an
internal node (its `val` may be anything) whose four children represent its four equal quadrants.

**Example**
```
Input:  grid = [[0,1],[1,0]]
Output: an internal node with four leaves 0, 1, 1, 0
```

**Constraints**
* `n == 2^x` with `0 <= x <= 6`

## Approach: Recursive quadrants

> If a square is uniform it becomes a leaf; otherwise split it into four quadrants and recurse.

**Build bottom-up by recursion.** `build(r, c, size)`: for size 1 return a leaf. Otherwise build the four quadrants; if all four are
leaves with the same value, merge them into one leaf, else return an internal node with those children.

* Time: **O(n²)** — every cell is visited once, and each internal node does O(1) merging work.
* Space: **O(log n)** — the recursion depth (plus the tree itself).

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0427/v1/ConstructQuadTree.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0427/v1/ConstructQuadTreeTest.java` | JUnit 6 tests |
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
