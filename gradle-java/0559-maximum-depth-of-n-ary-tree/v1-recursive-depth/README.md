# 559. Maximum Depth of N-ary Tree — v1: Recursive depth

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Tree &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/maximum-depth-of-n-ary-tree/)

## Problem

Return the maximum depth (number of nodes on the longest root-to-leaf path) of an n-ary tree.

The tree uses `NaryMaxDepth.Node`, which has `val` and `children`.

**Example**
```
1 → (3 → 5, 6), 2, 4   → 3
```

**Constraints**
* `0 <= n <= 10^4`, height at most 1000

## Approach: Recursive depth

> The depth of a node is one more than the deepest of its children.

**Recursion.** An empty tree has depth 0. Otherwise the depth is `1 + max(depth(child))` over the children (0 if there are none).

* Time: **O(n)**.
* Space: **O(h)** — recursion depth.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0559/v1/NaryMaxDepth.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0559/v1/NaryMaxDepthTest.java` | JUnit 6 tests |
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
