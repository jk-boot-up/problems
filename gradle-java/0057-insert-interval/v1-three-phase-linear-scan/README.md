# 57. Insert Interval — v1: Three-phase linear scan

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Intervals &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/insert-interval/)

## Problem

`intervals` is sorted by start and non-overlapping. Insert `newInterval` and merge where needed, so the result is still
sorted and non-overlapping. Return the result.

**Example 1**
```
Input:  intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]
```

**Example 2**
```
Input:  intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
```

**Constraints**
* `0 <= intervals.length <= 10^4`; `0 <= start <= end <= 10^5`

## Approach: Three-phase linear scan

> Copy intervals ending before the new one, merge every interval that overlaps it, then copy the rest.

**Three phases.** (1) Copy intervals whose end is before the new start. (2) While an interval starts at or before the new end,
merge it in: `start = min`, `end = max`. Add the merged interval. (3) Copy the rest.

* Time: **O(n)** — one pass.
* Space: **O(n)** — the output.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0057/v1/InsertInterval.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0057/v1/InsertIntervalTest.java` | JUnit 6 tests |
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
