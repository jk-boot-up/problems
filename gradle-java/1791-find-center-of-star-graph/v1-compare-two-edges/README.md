# 1791. Find Center of Star Graph — v1: Compare two edges

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Graph &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/find-center-of-star-graph/)

## Problem

An undirected **star** graph has one centre connected to every other node, and no other edges. Given its edges, return the centre.

**Example**
```
[[1,2],[2,3],[4,2]]       → 2
[[1,2],[5,1],[1,3],[1,4]] → 1
```

**Constraints**
* `3 <= n <= 10^5`; the input is a valid star

## Approach: Compare two edges

> The centre is in every edge, so it is the endpoint the first two edges share.

**Shared endpoint.** Every edge touches the centre and no other node appears twice, so the node common to `edges[0]` and `edges[1]` is the
centre.

* Time: **O(1)**.
* Space: **O(1)**.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p1791/v1/FindCenterOfStar.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p1791/v1/FindCenterOfStarTest.java` | JUnit 6 tests |
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
