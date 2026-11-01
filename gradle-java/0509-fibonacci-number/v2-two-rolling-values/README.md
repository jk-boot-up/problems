# 509. Fibonacci Number — v2: Two rolling values

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** 1D DP &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/fibonacci-number/)

## Problem

`F(0) = 0`, `F(1) = 1`, `F(n) = F(n-1) + F(n-2)`. Return `F(n)`.

**Example**
```
n = 2 → 1,   n = 3 → 2,   n = 4 → 3
```

**Constraints**
* `0 <= n <= 30`

## Approach: Two rolling values

> Each Fibonacci number is the sum of the previous two; keep two rolling values.

**Bottom-up.** Shift `(a, b)` forward `n` times.

* Time: **O(n)** — one loop.
* Space: **O(1)** — two ints.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0509/v2/FibonacciNumber.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0509/v2/FibonacciNumberTest.java` | JUnit 6 tests |
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

* [v1-naive-recursion](../v1-naive-recursion/README.md): Naive recursion (`O(2ⁿ)` time, `O(n)` space)
