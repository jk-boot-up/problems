# 1342. Number of Steps to Reduce a Number to Zero — v1: Simulation

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Bit Manipulation &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/)

## Problem

Repeatedly halve `num` if it is even, or subtract 1 if it is odd, until it is 0. Return the number of steps.

**Example**
```
14 → 6,   8 → 4,   123 → 12
```

**Constraints**
* `0 <= num <= 10^6`

## Approach: Simulation

> Each 1 bit costs a subtraction, and every bit except the top one costs a halving.

**Simulate.** At most about 2·log₂(num) steps. (Equivalently: bit length − 1 + number of 1 bits.)

* Time: **O(log n)** — number of bits.
* Space: **O(1)** — a counter.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p1342/v1/StepsToZero.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p1342/v1/StepsToZeroTest.java` | JUnit 6 tests |
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
