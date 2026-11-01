# 231. Power of Two — v1: Clear the lowest set bit

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Bit Manipulation &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/power-of-two/)

## Problem

Return `true` if `n` is a power of two, that is `n == 2^x` for some integer `x >= 0`.

**Example**
```
1  → true   (2^0)
16 → true
3  → false
```

**Constraints**
* `-2^31 <= n <= 2^31 - 1`

## Approach: Clear the lowest set bit

> A power of two has exactly one 1-bit, and n & (n − 1) clears the lowest 1-bit.

**One bit.** Powers of two are positive and have a single 1-bit. Subtracting 1 turns that bit off and every bit below it on, so
`n & (n - 1)` is 0 exactly for powers of two (and for 0, which the `n > 0` check excludes).

* Time: **O(1)**.
* Space: **O(1)**.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0231/v1/PowerOfTwo.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0231/v1/PowerOfTwoTest.java` | JUnit 6 tests |
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
