# 435. Non-overlapping Intervals — v1: Greedy by end

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Intervals &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/non-overlapping-intervals/)

## Problem

Return the minimum number of intervals to remove so the rest do not overlap (touching at an endpoint is fine).

**Example**
```
[[1,2],[2,3],[3,4],[1,3]] → 1
[[1,2],[1,2],[1,2]]       → 2
[[1,2],[2,3]]             → 0
```

**Constraints**
* `1 <= intervals.length <= 10^5`

## Approach: Greedy by end

> Keep intervals that end earliest; every interval overlapping the last kept one must be removed.

**Activity selection.** Sort by end. Keep an interval when it starts at or after the last kept end; otherwise remove it. Ending earliest
leaves the most room for the rest.

* Time: **O(n log n)** — sorting.
* Space: **O(log n)** — the sort's stack.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0435/v1/NonOverlappingIntervals.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0435/v1/NonOverlappingIntervalsTest.java` | JUnit 6 tests |
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
