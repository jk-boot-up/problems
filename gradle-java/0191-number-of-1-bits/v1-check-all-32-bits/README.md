# 191. Number of 1 Bits — v1: Check all 32 bits

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

## Approach: Check all 32 bits

> Test each of the 32 bits with a shift and a mask.

**Bit loop.** For `i = 0..31`, add `(n >>> i) & 1`.

* Time: **O(1)** — always 32 iterations.
* Space: **O(1)** — a counter.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0191/v1/NumberOf1Bits.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0191/v1/NumberOf1BitsTest.java` | JUnit 6 tests |
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

* [v2-clear-lowest-set-bit](../v2-clear-lowest-set-bit/README.md): Clear lowest set bit (`O(k)` time, `O(1)` space)
