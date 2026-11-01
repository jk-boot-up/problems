# 547. Number of Provinces — v1: Union-find

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Graph General &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/number-of-provinces/)

## Problem

`isConnected[i][j] = 1` means cities `i` and `j` are directly connected. A province is a group of directly or indirectly connected cities.
Return the number of provinces.

**Example**
```
[[1,1,0],[1,1,0],[0,0,1]] → 2,   [[1,0,0],[0,1,0],[0,0,1]] → 3
```

**Constraints**
* `1 <= n <= 200`

## Approach: Union-find

> Count connected components with union-find: every successful union merges two provinces.

**Disjoint sets.** Start with `n` provinces; for each connected pair `(i, j)` with `j > i`, a union of two different roots reduces the count.

* Time: **O(n²·α(n))** — every matrix cell is examined.
* Space: **O(n)** — the parent array.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0547/v1/NumberOfProvinces.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0547/v1/NumberOfProvincesTest.java` | JUnit 6 tests |
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
