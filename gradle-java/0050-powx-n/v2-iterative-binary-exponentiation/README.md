# 50. Pow(x, n) — v2: Iterative binary exponentiation

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Math &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/powx-n/)

## Problem

Implement `pow(x, n)`: `x` raised to the integer power `n` (which may be negative).

**Example**
```
pow(2.0, 10) = 1024.0,   pow(2.1, 3) = 9.261,   pow(2.0, -2) = 0.25
```

**Constraints**
* `-100.0 < x < 100.0`; `-2^31 <= n <= 2^31 - 1`; the result fits in a double.

## Approach: Iterative binary exponentiation

> Square the base and halve the exponent: each set bit of n multiplies one squared power into the result.

**Exponentiation by squaring.** Use `long e = n` (so `-Integer.MIN_VALUE` does not overflow); if negative, use `1/x` and `-e`.
While `e > 0`: if its lowest bit is set, multiply the result by the current base; square the base; shift `e` right.

* Time: **O(log n)** — one step per bit of n.
* Space: **O(1)** — a few variables.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0050/v2/PowXN.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0050/v2/PowXNTest.java` | JUnit 6 tests |
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

* [v1-recursive-fast-power](../v1-recursive-fast-power/README.md): Recursive fast power (`O(log n)` time, `O(log n)` space)
