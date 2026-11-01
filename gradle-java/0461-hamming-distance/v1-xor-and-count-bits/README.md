# 461. Hamming Distance — v1: XOR and count bits

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Bit Manipulation &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/hamming-distance/)

## Problem

Return the number of bit positions where `x` and `y` differ.

**Example**
```
x = 1, y = 4 → 2   (0001 vs 0100)
x = 3, y = 1 → 1
```

**Constraints**
* `0 <= x, y <= 2^31 - 1`

## Approach: XOR and count bits

> XOR leaves 1s exactly where the bits differ; count them.

**Kernighan's trick.** `z = x ^ y` has a 1 at each differing position. `z &= z - 1` clears the lowest 1-bit; count how many times until
`z` is 0.

* Time: **O(1)** — at most 31 iterations.
* Space: **O(1)**.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0461/v1/HammingDistance.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0461/v1/HammingDistanceTest.java` | JUnit 6 tests |
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
