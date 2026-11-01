# 621. Task Scheduler — v1: Greedy simulation with a max-heap

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

## Approach: Greedy simulation with a max-heap

> Each round of n + 1 slots, run the most frequent remaining tasks first.

**Simulation.** Keep counts in a max-heap. Each round, pop up to `n + 1` tasks, run them, and push back the ones with work left. A round
that is not the last counts `n + 1` intervals.

* Time: **O(N log 26)** — one heap operation per executed task.
* Space: **O(1)** — at most 26 heap entries.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0621/v1/TaskScheduler.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0621/v1/TaskSchedulerTest.java` | JUnit 6 tests |
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

* [v2-counting-formula](../v2-counting-formula/README.md): Counting formula (`O(N)` time, `O(1)` space)
