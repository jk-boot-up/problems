# 326. Power of Three — v1: Repeated division

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

## Approach: Repeated division

> Divide by 3 while it divides evenly; a power of three ends at 1.

**Loop.** For positive `n`, divide by 3 while `n % 3 == 0`, then check `n == 1`.

* Time: **O(log n)** — at most 19 divisions.
* Space: **O(1)**.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0326/v1/PowerOfThree.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0326/v1/PowerOfThreeTest.java` | JUnit 6 tests |
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

* [v2-divisor-of-3-19](../v2-divisor-of-3-19/README.md): Divisor of 3^19 (`O(1)` time, `O(1)` space)
