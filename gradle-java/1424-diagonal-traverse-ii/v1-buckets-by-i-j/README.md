# 1424. Diagonal Traverse II — v1: Buckets by i + j

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Matrix &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/diagonal-traverse-ii/)

## Problem

Given a jagged 2-D list `nums` (rows may have different lengths), return all elements in diagonal order: anti-diagonals `i + j = 0, 1, 2,
…`, each read from bottom-left to top-right.

**Example**
```
[[1,2,3],[4,5,6],[7,8,9]] → [1,4,2,7,5,3,8,6,9]
[[1,2,3,4,5],[6,7],[8],[9,10,11],[12,13,14,15,16]] → [1,6,2,8,7,3,9,4,12,10,5,13,11,14,15,16]
```

**Constraints**
* Up to `10^5` elements in total

## Approach: Buckets by i + j

> Cells on one anti-diagonal share i + j; bucket them, visiting rows bottom-up so each bucket is already in output order.

**Group by diagonal.** Element `(i, j)` belongs to diagonal `i + j`. Walk the rows from the **last** to the first and append each element to
its diagonal's bucket: within a bucket the larger `i` comes first, which is the bottom-left-to-top-right order. Concatenate the buckets.
Only existing cells are touched, which matters for very jagged input.

* Time: **O(N)** — `N` elements.
* Space: **O(N)** — the buckets.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p1424/v1/DiagonalTraverseII.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p1424/v1/DiagonalTraverseIITest.java` | JUnit 6 tests |
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
