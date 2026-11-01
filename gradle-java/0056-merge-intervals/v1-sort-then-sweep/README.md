# 56. Merge Intervals — v1: Sort, then sweep

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Intervals &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/merge-intervals/)

## Problem

Given an array of `intervals` where `intervals[i] = [start, end]`, merge all overlapping intervals and return the
non-overlapping intervals that cover exactly the same ranges.

**Example 1**
```
Input:  [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
```

**Example 2**
```
Input:  [[1,4],[4,5]]
Output: [[1,5]]   (touching intervals overlap)
```

**Constraints**
* `1 <= intervals.length <= 10^4`; `0 <= start <= end <= 10^4`

## Approach: Sort, then sweep

> Sort by start; each interval either overlaps the last merged one (extend it) or starts a new one.

**Sort and sweep.** Sort by start. Keep the last merged interval; if the next start is `<=` its end, extend the end to the
maximum of both ends. Otherwise append the next interval as a new merged interval.

* Time: **O(n log n)** — sorting; the sweep is linear.
* Space: **O(n)** — the output (plus the sort's stack).

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0056/v1/MergeIntervals.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0056/v1/MergeIntervalsTest.java` | JUnit 6 tests |
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
