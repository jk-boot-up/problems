# 1162. As Far from Land as Possible — v1: Multi-source BFS

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Graph BFS &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/as-far-from-land-as-possible/)

## Problem

In an `n × n` grid of `0` (water) and `1` (land), find a water cell whose Manhattan distance to the nearest land is as large as possible,
and return that distance. Return `-1` if there is no land or no water.

**Example**
```
[[1,0,1],[0,0,0],[1,0,1]] → 2
[[1,0,0],[0,0,0],[0,0,0]] → 4
```

**Constraints**
* `1 <= n <= 100`

## Approach: Multi-source BFS

> Multi-source BFS from all land cells at once; the last water cell reached is the farthest.

**All sources at once.** Put every land cell in the queue at distance 0 and BFS outward in 4 directions. On a grid without obstacles the
BFS distance equals the Manhattan distance to the nearest land. The number of BFS rounds needed to cover all water is the answer.

* Time: **O(n²)**.
* Space: **O(n²)**.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p1162/v1/AsFarFromLand.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p1162/v1/AsFarFromLandTest.java` | JUnit 6 tests |
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
