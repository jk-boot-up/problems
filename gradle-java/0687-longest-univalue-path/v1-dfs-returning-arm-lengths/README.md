# 687. Longest Univalue Path — v1: DFS returning arm lengths

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Binary Tree DFS &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/longest-univalue-path/)

## Problem

Return the length (number of **edges**) of the longest path in a binary tree where every node has the same value. The path need not pass
through the root.

**Example**
```
[5,4,5,1,1,null,5] → 2
[1,4,5,4,4,null,5] → 2
```

**Constraints**
* `0 <= n <= 10^4`

## Approach: DFS returning arm lengths

> Each node returns the longest same-value arm going down; a path can bend through a node using two arms.

**Arms.** `arm(node)` is the longest downward path of equal values starting at `node`. A child's arm counts (plus one edge) only if the
child has the same value. The best path bending at `node` uses both counted arms; record the maximum and return the longer arm.

* Time: **O(n)**.
* Space: **O(h)** — recursion depth.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0687/v1/LongestUnivaluePath.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0687/v1/LongestUnivaluePathTest.java` | JUnit 6 tests |
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
