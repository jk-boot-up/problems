# 1732. Find the Highest Altitude — v1: Running sum

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Prefix Sum &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/find-the-highest-altitude/)

## Problem

A biker starts at altitude 0; `gain[i]` is the change from point `i` to point `i + 1`. Return the highest altitude reached.

**Example**
```
[-5,1,5,0,-7] → 1,   [-4,-3,-2,-1,4,3,2] → 0
```

**Constraints**
* `1 <= n <= 100`

## Approach: Running sum

> Altitudes are running sums of the gains; return the largest running sum (starting at 0).

**Prefix sum.** Track the running altitude and its maximum, starting from 0.

* Time: **O(n)** — one pass.
* Space: **O(1)** — two numbers.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p1732/v1/HighestAltitude.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p1732/v1/HighestAltitudeTest.java` | JUnit 6 tests |
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
