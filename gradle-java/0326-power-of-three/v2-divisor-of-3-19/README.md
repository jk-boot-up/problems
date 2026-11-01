# 326. Power of Three — v2: Divisor of 3^19

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Math &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/power-of-three/)

## Problem

Return `true` if `n` is a power of three (`n == 3^x` for some integer `x >= 0`).

**Example**
```
27 → true
0  → false
-1 → false
45 → false
```

**Constraints**
* `-2^31 <= n <= 2^31 - 1`

## Approach: Divisor of 3^19

> 3^19 is the largest power of three in an int, and its only divisors are smaller powers of three.

**One modulo.** `3^19 = 1162261467` is the biggest power of three that fits in an `int`. Since 3 is prime, the positive divisors of
`3^19` are exactly `3^0 … 3^19`. So `n` is a power of three iff `n > 0` and `1162261467 % n == 0`.

* Time: **O(1)**.
* Space: **O(1)**.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0326/v2/PowerOfThree.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0326/v2/PowerOfThreeTest.java` | JUnit 6 tests |
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

* [v1-repeated-division](../v1-repeated-division/README.md): Repeated division (`O(log n)` time, `O(1)` space)
