# 746. Min Cost Climbing Stairs — v1: Two rolling values

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** 1D DP &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/min-cost-climbing-stairs/)

## Problem

`cost[i]` is the price of stepping off stair `i`; from there you climb 1 or 2 stairs. You may start at stair 0 or 1. Return the minimum cost
to reach the top (just past the last stair).

**Example**
```
[10,15,20] → 15,   [1,100,1,1,1,100,1,1,100,1] → 6
```

**Constraints**
* `2 <= cost.length <= 1000`

## Approach: Two rolling values

> Reaching step i costs the cheaper of coming from i−1 or i−2, plus what you pay to leave that step.

**DP.** `reach(i) = min(reach(i-1) + cost[i-1], reach(i-2) + cost[i-2])` with `reach(0) = reach(1) = 0`; answer `reach(n)`.

* Time: **O(n)** — one pass.
* Space: **O(1)** — two values.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0746/v1/MinCostClimbingStairs.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0746/v1/MinCostClimbingStairsTest.java` | JUnit 6 tests |
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
