# 118. Pascal's Triangle — v1: Row by row

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** 1D DP &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/pascals-triangle/)

## Problem

Return the first `numRows` rows of Pascal's triangle.

**Example**
```
numRows = 5 → [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
```

**Constraints**
* `1 <= numRows <= 30`

## Approach: Row by row

> Each inner value is the sum of the two values above it; every row starts and ends with 1.

**Build from the previous row.** Row `i` has `i + 1` values: 1 at both ends, `prev[j-1] + prev[j]` in between.

* Time: **O(n²)** — n rows of up to n values.
* Space: **O(1)** — apart from the output.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0118/v1/PascalsTriangle.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0118/v1/PascalsTriangleTest.java` | JUnit 6 tests |
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
