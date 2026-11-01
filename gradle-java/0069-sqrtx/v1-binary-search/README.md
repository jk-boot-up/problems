# 69. Sqrt(x) — v1: Binary search

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Math &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/sqrtx/)

## Problem

Given a non-negative integer `x`, return the square root of `x` rounded **down** to an integer, without using built-in power or square
root functions.

**Example**
```
4 → 2,   8 → 2 (2.828…)
```

**Constraints**
* `0 <= x <= 2^31 - 1`

## Approach: Binary search

> Search for the largest m with m × m ≤ x.

**Binary search on the answer.** Search `[0, x]`; if `mid * mid <= x` (as `long`), the answer is at least `mid`.

* Time: **O(log x)** — the range halves each step.
* Space: **O(1)** — a few longs.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0069/v1/SqrtX.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0069/v1/SqrtXTest.java` | JUnit 6 tests |
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

* [v2-newton-s-method](../v2-newton-s-method/README.md): Newton's method (`O(log x)` time, `O(1)` space)
