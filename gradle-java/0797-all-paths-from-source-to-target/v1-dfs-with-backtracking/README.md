# 797. All Paths From Source to Target — v1: DFS with backtracking

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Backtracking &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/all-paths-from-source-to-target/)

## Problem

Given a **DAG** of `n` nodes where `graph[i]` lists the nodes reachable from `i`, return every path from node `0` to node `n - 1`, in any order.

**Example**
```
[[1,2],[3],[3],[]]           → [[0,1,3],[0,2,3]]
[[4,3,1],[3,2,4],[3],[4],[]] → [[0,4],[0,3,4],[0,1,3,4],[0,1,2,3,4],[0,1,4]]
```

**Constraints**
* `2 <= n <= 15`; no cycles.

## Approach: DFS with backtracking

> DFS from node 0 over the DAG, recording the path whenever it reaches node n − 1.

**Backtracking.** Extend the path with each next node; at `n - 1`, record a copy. No visited set is needed because the graph has no cycles.

* Time: **O(2ⁿ · n)** — up to 2ⁿ⁻² paths, each copied in O(n).
* Space: **O(n)** — the path and recursion.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0797/v1/AllPathsSourceTarget.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0797/v1/AllPathsSourceTargetTest.java` | JUnit 6 tests |
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
