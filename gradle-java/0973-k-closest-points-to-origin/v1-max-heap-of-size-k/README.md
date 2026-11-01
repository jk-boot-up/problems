# 973. K Closest Points to Origin — v1: Max-heap of size k

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Heap &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/k-closest-points-to-origin/)

## Problem

Return the `k` points closest to the origin `(0, 0)` by Euclidean distance, in any order.

**Example**
```
points = [[1,3],[-2,2]], k = 1          → [[-2,2]]
points = [[3,3],[5,-1],[-2,4]], k = 2   → [[3,3],[-2,4]]
```

**Constraints**
* `1 <= k <= points.length <= 10^4`

## Approach: Max-heap of size k

> Keep a max-heap of the k closest points seen so far; a closer point replaces the farthest one.

**Bounded max-heap by squared distance.** Push each point; if the heap holds more than `k`, pop the farthest. Squared distances avoid
square roots and stay exact.

* Time: **O(n log k)** — n heap operations of size k.
* Space: **O(k)** — the heap.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0973/v1/KClosestPoints.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0973/v1/KClosestPointsTest.java` | JUnit 6 tests |
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
