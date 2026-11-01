# 399. Evaluate Division — v1: Weighted union-find

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Graph General &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/evaluate-division/)

## Problem

You are given equations `Ai / Bi = values[i]` between variables (strings). For each query `Cj / Dj`, return its value, or `-1.0` if it
cannot be determined. Variables that never appear in an equation are unknown (even `x / x` gives `-1.0`). There are no contradictions
or divisions by zero.

**Example**
```
Input:  equations = [["a","b"],["b","c"]], values = [2.0,3.0]
        queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
Output: [6.0, 0.5, -1.0, 1.0, -1.0]
```

**Constraints**
* `1 <= equations.length, queries.length <= 20`; `0 < values[i] <= 20`

## Approach: Weighted union-find

> Keep each variable's ratio to its group root; two variables in the same group divide via their ratios.

**Union-find with weights.** `parent[x]` and `weight[x] = x / parent[x]`. `find` compresses paths and multiplies weights so each
variable stores its ratio to the root. For `a / b = k`, join the roots so the ratios stay consistent. A query `c / d` is
`weight[c] / weight[d]` when both share a root. Both maps are `MyHashMap`s.

* Time: **O((E + Q)·α(V))** — almost constant per operation thanks to path compression.
* Space: **O(V)** — the parent and weight maps.

Hash lookups use `MyHashMap` / `MyHashSet`, our own hash table (bucket array, chaining, resizing), instead of `java.util.HashMap`.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0399/v1/EvaluateDivision.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0399/v1/EvaluateDivisionTest.java` | JUnit 6 tests |
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

* [v2-weighted-graph-dfs](../v2-weighted-graph-dfs/README.md): Weighted graph + DFS (`O(Q·(V + E))` time, `O(V + E)` space)
