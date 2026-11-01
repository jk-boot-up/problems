# 218. The Skyline Problem — v1: Height at every edge

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

## Approach: Height at every edge

> For each edge x, scan all buildings to find the tallest one covering x.

**Brute force.** The height just right of `x` is the tallest building with `left <= x < right`. Compute it for every distinct edge by
scanning all buildings, and keep the points where it changes.

* Time: **O(n²)** — `2n` edges, each scanning `n` buildings.
* Space: **O(n)** — the edge list.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0218/v1/Skyline.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0218/v1/SkylineTest.java` | JUnit 6 tests |
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

* [v2-sweep-line-with-a-max-heap](../v2-sweep-line-with-a-max-heap/README.md): Sweep line with a max-heap (`O(n log n)` time, `O(n)` space)
