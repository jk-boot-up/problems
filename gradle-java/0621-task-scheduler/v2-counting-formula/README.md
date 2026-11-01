# 621. Task Scheduler — v2: Counting formula

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Heap &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/task-scheduler/)

## Problem

CPU tasks are letters; each takes one interval. The same task must be separated by at least `n` intervals (idle intervals allowed).
Return the minimum number of intervals to finish all tasks.

**Example**
```
tasks = [A,A,A,B,B,B], n = 2 → 8   (A B idle A B idle A B)
tasks = [A,C,A,B,D,B], n = 1 → 6
```

**Constraints**
* `1 <= tasks.length <= 10^4`; `0 <= n <= 100`

## Approach: Counting formula

> The most frequent task fixes a frame of (maxCount − 1) blocks of n + 1 slots; the others fill the gaps.

**Frame counting.** Let `maxCount` be the highest frequency and `tied` the number of tasks with that frequency. The busiest task needs
`(maxCount - 1)` full blocks of `n + 1` slots plus a final block of `tied` slots. If there are more tasks than that, no idle time is needed:
the answer is `max(tasks.length, (maxCount - 1) * (n + 1) + tied)`.

* Time: **O(N)** — one counting pass.
* Space: **O(1)** — 26 counters.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0621/v2/TaskScheduler.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0621/v2/TaskSchedulerTest.java` | JUnit 6 tests |
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

* [v1-greedy-simulation-with-a-max-heap](../v1-greedy-simulation-with-a-max-heap/README.md): Greedy simulation with a max-heap (`O(N log 26)` time, `O(1)` space)
