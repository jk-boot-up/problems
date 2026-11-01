# 1609. Even Odd Tree — v1: Level-order checks

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Binary Tree BFS &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/even-odd-tree/)

## Problem

A tree is **Even-Odd** if, with the root at level 0:

* on even levels, all values are **odd** and strictly increasing left to right;
* on odd levels, all values are **even** and strictly decreasing left to right.

Return whether the tree is Even-Odd.

**Example**
```
[1,10,4,3,null,7,9,12,8,6,null,null,2] → true
[5,4,2,3,3,7]                           → false
[5,9,1,3,5,7]                           → false
```

**Constraints**
* `1 <= n <= 10^5`

## Approach: Level-order checks

> Check each level during a BFS: parity of every value and strict direction of the sequence.

**BFS per level.** Walk each level left to right, remembering the previous value. On even levels require `val` odd and `val > prev`; on odd
levels require `val` even and `val < prev`. Fail fast on the first violation.

* Time: **O(n)**.
* Space: **O(w)** — the widest level.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p1609/v1/EvenOddTree.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p1609/v1/EvenOddTreeTest.java` | JUnit 6 tests |
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
