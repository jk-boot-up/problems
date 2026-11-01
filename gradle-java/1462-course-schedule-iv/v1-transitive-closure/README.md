# 1462. Course Schedule IV — v1: Transitive closure

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Graph &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/course-schedule-iv/)

## Problem

There are `numCourses` courses. `prerequisites[i] = [a, b]` means `a` must be taken before `b`. Prerequisites are transitive. For each
query `[u, v]`, return whether `u` is a (direct or indirect) prerequisite of `v`.

**Example**
```
numCourses = 2, prerequisites = [[1,0]], queries = [[0,1],[1,0]] → [false,true]
numCourses = 3, prerequisites = [[1,2],[1,0],[2,0]], queries = [[1,0],[1,2]] → [true,true]
```

**Constraints**
* `2 <= numCourses <= 100`, no cycles, up to `10^4` queries

## Approach: Transitive closure

> With at most 100 courses, precompute every reachable pair with Floyd–Warshall style closure.

**Closure.** `reach[a][b]` starts true for direct prerequisites. For every middle course `k`, if `a` reaches `k` and `k` reaches `b`, then `a`
reaches `b`. After all `k`, each query is a lookup.

* Time: **O(n³ + q)**.
* Space: **O(n²)**.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p1462/v1/CourseScheduleIV.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p1462/v1/CourseScheduleIVTest.java` | JUnit 6 tests |
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
