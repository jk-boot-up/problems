# 1351. Count Negative Numbers in a Sorted Matrix — v1: Staircase walk

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Matrix &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/)

## Problem

A matrix is sorted in **non-increasing** order along every row and every column. Count its negative numbers.

**Example**
```
[[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]] → 8
[[3,2],[1,0]] → 0
```

**Constraints**
* `1 <= m, n <= 100`

## Approach: Staircase walk

> Rows and columns are non-increasing, so the boundary of the negatives is a staircase you can walk in m + n steps.

**Staircase.** Start at the bottom-left. If the value is negative, everything to its right in that row is too: add `n - col` and move up.
Otherwise move right. Each step leaves a row or a column for good.

* Time: **O(m + n)**.
* Space: **O(1)**.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p1351/v1/CountNegatives.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p1351/v1/CountNegativesTest.java` | JUnit 6 tests |
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
