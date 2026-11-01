# 371. Sum of Two Integers — v1: XOR and carry

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Bit Manipulation &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/sum-of-two-integers/)

## Problem

Return `a + b` without using the `+` or `-` operators.

**Example**
```
1 + 2 = 3,   2 + 3 = 5,   -1 + 1 = 0
```

**Constraints**
* `-1000 <= a, b <= 1000`

## Approach: XOR and carry

> XOR adds without carries, AND shifted left gives the carries; repeat until no carry remains.

**Binary addition.** `a ^ b` is the sum ignoring carries; `(a & b) << 1` is the carry. Replace `a` with the partial sum and `b` with the
carry until the carry is 0. Two's complement makes negative numbers work too (Java ints wrap).

* Time: **O(1)** — at most 32 iterations.
* Space: **O(1)** — two ints.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0371/v1/SumOfTwoIntegers.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0371/v1/SumOfTwoIntegersTest.java` | JUnit 6 tests |
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
