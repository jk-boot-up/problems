# 509. Fibonacci Number — v1: Naive recursion

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** 1D DP &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/fibonacci-number/)

## Problem

`F(0) = 0`, `F(1) = 1`, `F(n) = F(n-1) + F(n-2)`. Return `F(n)`.

**Example**
```
n = 2 → 1,   n = 3 → 2,   n = 4 → 3
```

**Constraints**
* `0 <= n <= 30`

## Approach: Naive recursion

> F(n) = F(n−1) + F(n−2) computed directly, re-solving the same subproblems many times.

**Plain recursion.** Mirrors the definition but recomputes overlapping subproblems.

* Time: **O(2ⁿ)** — the call tree roughly doubles at each level.
* Space: **O(n)** — the recursion depth.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0509/v1/FibonacciNumber.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0509/v1/FibonacciNumberTest.java` | JUnit 6 tests |
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

* [v2-two-rolling-values](../v2-two-rolling-values/README.md): Two rolling values (`O(n)` time, `O(1)` space)
