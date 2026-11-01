# 463. Island Perimeter — v1: Count cells and shared edges

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Matrix &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/island-perimeter/)

## Problem

A grid of `1` (land) and `0` (water) contains exactly one island with no lakes. Return the island's perimeter.

**Example**
```
0 1 0 0
1 1 1 0    → 16
0 1 0 0
1 1 0 0
```

**Constraints**
* `1 <= rows, cols <= 100`

## Approach: Count cells and shared edges

> Each land cell adds 4 edges; each pair of touching land cells hides 2 of them.

**Edges.** Every land cell has 4 sides. Each shared side between two land cells is counted once by each and is not part of the
perimeter. Count land cells and neighbours above and to the left: `4 · land - 2 · shared`.

* Time: **O(mn)**.
* Space: **O(1)**.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0463/v1/IslandPerimeter.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0463/v1/IslandPerimeterTest.java` | JUnit 6 tests |
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
