# 1971. Find if Path Exists in Graph — v1: Union–find

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Union Find &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/find-if-path-exists-in-graph/)

## Problem

Given an undirected graph with `n` nodes and a list of edges, return whether there is a path from `source` to `destination`.

**Example**
```
n = 3, edges = [[0,1],[1,2],[2,0]], source = 0, destination = 2 → true
n = 6, edges = [[0,1],[0,2],[3,5],[5,4],[4,3]], source = 0, destination = 5 → false
```

**Constraints**
* `1 <= n <= 2 * 10^5`, up to `2 * 10^5` edges

## Approach: Union–find

> Union the endpoints of every edge; a path exists iff source and destination end up in the same set.

**Disjoint sets.** Start with every node in its own set. For each edge, merge the two endpoints' sets (union by size, with path halving in
`find`). Afterwards, compare the roots of `source` and `destination`.

* Time: **O((n + E) · α(n))** — practically linear.
* Space: **O(n)**.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p1971/v1/FindIfPathExists.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p1971/v1/FindIfPathExistsTest.java` | JUnit 6 tests |
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
