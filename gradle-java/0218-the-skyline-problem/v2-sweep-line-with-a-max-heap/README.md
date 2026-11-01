# 218. The Skyline Problem — v2: Sweep line with a max-heap

**Difficulty:** Hard &nbsp;|&nbsp; **Topic:** Heap &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/the-skyline-problem/)

## Problem

Each building is `[left, right, height]`, sorted by `left`. Return the **skyline**: the key points `[x, height]` where the outline's height
changes, sorted by `x`. The last point always has height 0. No two consecutive points may have the same height.

**Example**
```
[[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]
  → [[2,10],[3,15],[7,12],[12,0],[15,10],[20,8],[24,0]]
[[0,2,3],[2,5,3]] → [[0,3],[5,0]]
```

**Constraints**
* `1 <= buildings.length <= 10^4`, `0 <= left < right <= 2^31 - 1`, `1 <= height <= 2^31 - 1`

## Approach: Sweep line with a max-heap

> Sweep the x-coordinates; a max-heap of active buildings gives the current height, and every change is a key point.

**Sweep.** The height can only change at a building edge. Visit the distinct edge x-coordinates in order. Push every building that starts
at or before `x` into a max-heap keyed by height, then pop buildings from the top whose `right <= x` (lazy removal: buried finished
buildings are removed once they reach the top). The heap top is the height just right of `x`; record `[x, h]` if it differs from the
last recorded height.

* Time: **O(n log n)** — sorting edges and heap operations.
* Space: **O(n)** — the heap and edge list.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0218/v2/Skyline.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0218/v2/SkylineTest.java` | JUnit 6 tests |
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
* **Complexity:** time and space cost, plotted against the common growth curves, and compared with the other approaches.

Switch between Light, Medium and Dark themes in the header.

## Other approaches

* [v1-height-at-every-edge](../v1-height-at-every-edge/README.md): Height at every edge (`O(n²)` time, `O(n)` space)
