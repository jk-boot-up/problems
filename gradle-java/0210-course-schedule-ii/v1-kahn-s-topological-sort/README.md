# 210. Course Schedule II — v1: Kahn's topological sort

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Graph General &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/course-schedule-ii/)

## Problem

Same setup as Course Schedule: `prerequisites[i] = [a, b]` means `b` before `a`. Return **an ordering** of all courses that respects
every prerequisite, or an empty array if impossible. Any valid order is accepted.

**Example 1**
```
Input:  numCourses = 2, prerequisites = [[1,0]]
Output: [0,1]
```

**Example 2**
```
Input:  numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
Output: [0,1,2,3] or [0,2,1,3]
```

**Constraints**
* `1 <= numCourses <= 2000`; pairs are unique.

## Approach: Kahn's topological sort

> Kahn's algorithm produces a valid order directly: the order in which courses become ready.

**Kahn's algorithm, recording the order.** Repeatedly take a course with in-degree 0, append it to the answer, and decrement its
dependants. If fewer than `numCourses` were taken, there is a cycle: return `[]`.

* Time: **O(V + E)** — each course and edge is processed once.
* Space: **O(V + E)** — adjacency lists, in-degrees, the queue.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0210/v1/CourseScheduleII.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0210/v1/CourseScheduleIITest.java` | JUnit 6 tests |
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
