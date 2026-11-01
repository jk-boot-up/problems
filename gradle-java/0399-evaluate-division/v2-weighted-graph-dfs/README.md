# 399. Evaluate Division — v2: Weighted graph + DFS

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

## Approach: Weighted graph + DFS

> Each equation a / b = k is an edge a → b with weight k (and b → a with 1/k); a query is a path product.

**Graph search.** Build `MyHashMap<String, MyHashMap<String, Double>>` with an edge `a → b` of weight `k` and `b → a` of weight
`1/k`. For each query, DFS from `C` to `D` multiplying weights along the path, with a `MyHashSet` of visited variables.

* Time: **O(Q·(V + E))** — one graph search per query.
* Space: **O(V + E)** — the adjacency maps.

Hash lookups use `MyHashMap` / `MyHashSet`, our own hash table (bucket array, chaining, resizing), instead of `java.util.HashMap`.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0399/v2/EvaluateDivision.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0399/v2/EvaluateDivisionTest.java` | JUnit 6 tests |
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

* [v1-weighted-union-find](../v1-weighted-union-find/README.md): Weighted union-find (`O((E + Q)·α(V))` time, `O(V)` space)
