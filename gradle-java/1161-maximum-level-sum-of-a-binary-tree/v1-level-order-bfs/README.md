# 1161. Maximum Level Sum of a Binary Tree — v1: Level-order BFS

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Binary Tree BFS &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/)

## Problem

The root is level 1, its children level 2, and so on. Return the smallest level whose node values have the maximal sum.

**Example**
```
[1,7,0,7,-8,null,null] → 2,   [989,null,10250,98693,-89388,null,null,null,-32127] → 2
```

**Constraints**
* `1 <= n <= 10^4`

## Approach: Level-order BFS

> Sum each level with BFS and keep the smallest level number with the largest sum.

**BFS by levels.** Sum each level; update the answer only on a strictly larger sum, so ties keep the smaller level.

* Time: **O(n)** — each node once.
* Space: **O(w)** — the widest level.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p1161/v1/MaximumLevelSum.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p1161/v1/MaximumLevelSumTest.java` | JUnit 6 tests |
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
