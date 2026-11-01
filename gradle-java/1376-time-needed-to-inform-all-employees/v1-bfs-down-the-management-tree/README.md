# 1376. Time Needed to Inform All Employees — v1: BFS down the management tree

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Tree &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/time-needed-to-inform-all-employees/)

## Problem

A company has `n` employees; `manager[i]` is the direct manager of `i` (`-1` for the head, `headID`). Starting with the head, each manager
needs `informTime[i]` minutes to tell all direct reports, who then pass it on. Return the minutes until everyone knows.

**Example**
```
n = 6, headID = 2, manager = [2,2,-1,2,2,2], informTime = [0,0,1,0,0,0] → 1
n = 7, headID = 6, manager = [1,2,3,4,5,6,-1], informTime = [0,6,5,4,3,2,1] → 21
```

**Constraints**
* `1 <= n <= 10^5`

## Approach: BFS down the management tree

> The company is a tree rooted at the head; the answer is the slowest root-to-leaf chain of inform times.

**Tree paths.** Build child lists from `manager` (as linked arrays, so no per-node lists). Traverse from the head with a queue, carrying the
time at which each employee hears the news: a child hears at `time[parent] + informTime[parent]`. The answer is the latest time. Iteration
avoids deep recursion on a 10⁵-long chain.

* Time: **O(n)**.
* Space: **O(n)**.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p1376/v1/TimeToInform.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p1376/v1/TimeToInformTest.java` | JUnit 6 tests |
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
