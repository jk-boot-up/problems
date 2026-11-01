# 684. Redundant Connection — v1: Union-find

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Graph General &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/redundant-connection/)

## Problem

A tree on nodes `1..n` had one extra edge added. Given the `n` edges, return an edge that can be removed so the graph becomes a tree; if
several work, return the one that appears last in the input.

**Example**
```
[[1,2],[1,3],[2,3]]                 → [2,3]
[[1,2],[2,3],[3,4],[1,4],[1,5]]     → [1,4]
```

**Constraints**
* `3 <= n <= 1000`

## Approach: Union-find

> Union-find: the first edge whose endpoints are already connected closes the cycle.

**Disjoint sets.** Process edges in order; `union(a, b)` fails exactly when `a` and `b` already share a root, so that edge is redundant
(and it is the last edge of the cycle in input order). Path compression and union by size keep operations nearly O(1).

* Time: **O(n·α(n))** — essentially linear.
* Space: **O(n)** — the parent array.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0684/v1/RedundantConnection.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0684/v1/RedundantConnectionTest.java` | JUnit 6 tests |
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
