# 50. Pow(x, n) — v1: Recursive fast power

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Math &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/powx-n/)

## Problem

Implement `pow(x, n)`: `x` raised to the integer power `n` (which may be negative).

**Example**
```
pow(2.0, 10) = 1024.0,   pow(2.1, 3) = 9.261,   pow(2.0, -2) = 0.25
```

**Constraints**
* `-100.0 < x < 100.0`; `-2^31 <= n <= 2^31 - 1`; the result fits in a double.

## Approach: Recursive fast power

> xⁿ = (x^(n/2))², times x when n is odd.

**Divide and conquer.** `pow(x, n) = half * half` (times `x` if `n` is odd), where `half = pow(x, n / 2)`.

* Time: **O(log n)** — the exponent halves each call.
* Space: **O(log n)** — the recursion depth.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0050/v1/PowXN.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0050/v1/PowXNTest.java` | JUnit 6 tests |
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

* [v2-iterative-binary-exponentiation](../v2-iterative-binary-exponentiation/README.md): Iterative binary exponentiation (`O(log n)` time, `O(1)` space)
