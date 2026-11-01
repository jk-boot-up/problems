# 207. Course Schedule — v2: Kahn's topological sort

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

## Approach: Kahn's topological sort

> Courses can all be finished exactly when the prerequisite graph has no cycle; peel off courses with no remaining prerequisites.

**Kahn's algorithm.** Count each course's unmet prerequisites (in-degree). Queue every course with in-degree 0; when a course is
taken, decrement its dependants and queue any that reach 0. All courses are taken iff there is no cycle.

* Time: **O(V + E)** — each course and edge is processed once.
* Space: **O(V + E)** — the adjacency lists and the queue.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0207/v2/CourseSchedule.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0207/v2/CourseScheduleTest.java` | JUnit 6 tests |
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

* [v1-dfs-cycle-detection](../v1-dfs-cycle-detection/README.md): DFS cycle detection (`O(V + E)` time, `O(V + E)` space)
