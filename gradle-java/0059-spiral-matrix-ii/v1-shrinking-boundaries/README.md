# 59. Spiral Matrix II — v1: Shrinking boundaries

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Matrix &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/spiral-matrix-ii/)

## Problem

Generate an `n × n` matrix filled with `1 .. n²` in clockwise spiral order.

**Example**
```
n = 3 → [[1,2,3],[8,9,4],[7,6,5]]
```

**Constraints**
* `1 <= n <= 20`

## Approach: Shrinking boundaries

> Walk the four shrinking boundaries clockwise, writing 1, 2, 3, … as you go.

**Boundaries.** Fill the top row left→right, right column top→bottom, bottom row right→left, left column bottom→top; shrink and repeat.

* Time: **O(n²)** — each cell once.
* Space: **O(1)** — apart from the output.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0059/v1/SpiralMatrixII.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0059/v1/SpiralMatrixIITest.java` | JUnit 6 tests |
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
