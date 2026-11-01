# 62. Unique Paths — v1: Combinatorics

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Multidimensional DP &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/unique-paths/)

## Problem

A robot on an `m × n` grid starts at the top-left and moves only right or down. How many unique paths reach the bottom-right corner?

**Example**
```
m = 3, n = 7 → 28,   m = 3, n = 2 → 3
```

**Constraints**
* `1 <= m, n <= 100`; the answer fits in 32 bits.

## Approach: Combinatorics

> Every path is a sequence of (m−1) downs and (n−1) rights: choose where the downs go.

**Binomial coefficient.** The answer is `C(m + n - 2, m - 1)`; compute it incrementally with `long` to avoid overflow.

* Time: **O(min(m, n))** — one multiplication per step.
* Space: **O(1)** — one long.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0062/v1/UniquePaths.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0062/v1/UniquePathsTest.java` | JUnit 6 tests |
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

* [v2-one-rolling-row](../v2-one-rolling-row/README.md): One rolling row (`O(m·n)` time, `O(n)` space)
