# 452. Minimum Number of Arrows to Burst Balloons — v1: Greedy by end point

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Intervals &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/)

## Problem

Balloons are horizontal intervals `points[i] = [xstart, xend]` on a wall. A vertical arrow shot at `x` bursts every balloon with
`xstart <= x <= xend`. Return the **minimum** number of arrows needed to burst all balloons.

**Example 1**
```
Input:  points = [[10,16],[2,8],[1,6],[7,12]]
Output: 2   (shoot at x = 6 and x = 11)
```

**Example 2**
```
Input:  points = [[1,2],[3,4],[5,6],[7,8]]
Output: 4
```

**Example 3**
```
Input:  points = [[1,2],[2,3],[3,4],[4,5]]
Output: 2
```

**Constraints**
* `1 <= points.length <= 10^5`; `-2^31 <= xstart < xend <= 2^31 - 1`

## Approach: Greedy by end point

> Sort balloons by right edge; shoot at the first right edge and skip every balloon that arrow already pierces.

**Greedy.** Sort by end. Shoot the first arrow at the smallest end: it is as far right as possible while still hitting that balloon.
Every balloon starting at or before the arrow is burst. The first balloon starting after it needs a new arrow at its end.
Compare with `Integer.compare` to avoid overflow.

* Time: **O(n log n)** — sorting; the sweep is linear.
* Space: **O(log n)** — the sort's recursion stack.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0452/v1/MinimumArrows.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0452/v1/MinimumArrowsTest.java` | JUnit 6 tests |
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
