# 191. Number of 1 Bits — v2: Clear lowest set bit

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Bit Manipulation &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/number-of-1-bits/)

## Problem

Return the number of set bits (`1`s) in the binary representation of a positive integer `n` (its Hamming weight).

**Example**
```
n = 11 (1011)            → 3
n = 128 (10000000)       → 1
n = 2147483645           → 30
```

**Constraints**
* `1 <= n <= 2^31 - 1`

## Approach: Clear lowest set bit

> n & (n − 1) clears the lowest set bit, so count how many times you can do that before n is 0.

**Brian Kernighan's trick.** `n & (n - 1)` turns off the lowest 1-bit. Loop until `n == 0`, counting iterations.

* Time: **O(k)** — k is the number of set bits (at most 32).
* Space: **O(1)** — a counter.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0191/v2/NumberOf1Bits.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0191/v2/NumberOf1BitsTest.java` | JUnit 6 tests |
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

* [v1-check-all-32-bits](../v1-check-all-32-bits/README.md): Check all 32 bits (`O(1)` time, `O(1)` space)
