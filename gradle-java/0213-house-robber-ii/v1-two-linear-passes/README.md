# 213. House Robber II — v1: Two linear passes

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** 1D DP &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/house-robber-ii/)

## Problem

Same as House Robber, but the houses are arranged in a **circle**: the first and last houses are neighbours. Return the maximum amount.

**Example**
```
[2,3,2] → 3,   [1,2,3,1] → 4,   [1,2,3] → 3
```

**Constraints**
* `1 <= nums.length <= 100`

## Approach: Two linear passes

> The houses form a circle, so the first and last can't both be robbed: solve the line twice, without each end.

**Break the circle.** Either the first house is skipped (rob from `1..n-1`) or the last is (rob from `0..n-2`). Run the linear
House Robber on both ranges and take the larger. A single house is a special case.

* Time: **O(n)** — two linear passes.
* Space: **O(1)** — two variables per pass.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0213/v1/HouseRobberII.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0213/v1/HouseRobberIITest.java` | JUnit 6 tests |
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
