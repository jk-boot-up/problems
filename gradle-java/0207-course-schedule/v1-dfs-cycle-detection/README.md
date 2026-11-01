# 207. Course Schedule — v1: DFS cycle detection

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Graph General &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/course-schedule/)

## Problem

There are `numCourses` courses `0..numCourses-1`. `prerequisites[i] = [a, b]` means you must take `b` before `a`. Return `true` if
it is possible to finish all courses.

**Example 1**
```
Input:  numCourses = 2, prerequisites = [[1,0]]
Output: true
```

**Example 2**
```
Input:  numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false   (a cycle)
```

**Constraints**
* `1 <= numCourses <= 2000`; `0 <= prerequisites.length <= 5000`; pairs are unique.

## Approach: DFS cycle detection

> Colour courses white, grey (on the current DFS path) and black (done); reaching a grey course means a cycle.

**Three-colour DFS.** Start a DFS from every unvisited course. Mark it grey on entry and black on exit. An edge into a grey course
closes a cycle.

* Time: **O(V + E)** — each course and edge is explored once.
* Space: **O(V + E)** — the adjacency lists and the recursion stack.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0207/v1/CourseSchedule.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0207/v1/CourseScheduleTest.java` | JUnit 6 tests |
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

* [v2-kahn-s-topological-sort](../v2-kahn-s-topological-sort/README.md): Kahn's topological sort (`O(V + E)` time, `O(V + E)` space)
