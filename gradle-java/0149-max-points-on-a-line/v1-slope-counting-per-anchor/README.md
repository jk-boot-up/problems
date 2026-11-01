# 149. Max Points on a Line — v1: Slope counting per anchor

**Difficulty:** Hard &nbsp;|&nbsp; **Topic:** Math &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/max-points-on-a-line/)

## Problem

Given an array of distinct `points[i] = [x, y]`, return the maximum number of points that lie on the same straight line.

**Example**
```
[[1,1],[2,2],[3,3]] → 3
[[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]] → 4
```

**Constraints**
* `1 <= points.length <= 300`; `-10^4 <= x, y <= 10^4`; all points are distinct.

## Approach: Slope counting per anchor

> Fix each point and count the others by exact slope (a reduced fraction) in a hash map.

**Exact slopes.** For each anchor point `i`, compute `dx, dy` to every later point, divide both by `gcd(|dx|, |dy|)` and normalize the
sign (so `(1,2)` and `(-1,-2)` match, and vertical lines become `(0,1)`). Count slopes in a `MyHashMap`; the best line through `i`
has `1 + max count` points. Using fractions avoids floating-point errors.

* Time: **O(n² log C)** — n²/2 pairs, each with a gcd on coordinates up to C.
* Space: **O(n)** — the slope map for one anchor.

Hash lookups use `MyHashMap` / `MyHashSet`, our own hash table (bucket array, chaining, resizing), instead of `java.util.HashMap`.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0149/v1/MaxPointsOnALine.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0149/v1/MaxPointsOnALineTest.java` | JUnit 6 tests |
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
