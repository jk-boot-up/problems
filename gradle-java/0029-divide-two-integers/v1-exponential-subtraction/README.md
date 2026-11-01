# 29. Divide Two Integers — v1: Exponential subtraction

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Bit Manipulation &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/divide-two-integers/)

## Problem

Divide two integers **without** using multiplication, division or mod. The quotient truncates toward zero. If the result overflows 32 bits,
return `2^31 - 1`.

**Example**
```
10 / 3 = 3,   7 / -3 = -2,   -2147483648 / -1 = 2147483647
```

**Constraints**
* `-2^31 <= dividend, divisor <= 2^31 - 1`; `divisor != 0`

## Approach: Exponential subtraction

> Subtract the largest doubled divisor (divisor·2^k) that still fits, adding 2^k to the quotient each time.

**Doubling.** Work with negative numbers (they have the larger range). Repeatedly find the largest `divisor << k` that still fits in the
remaining dividend, subtract it and add `1 << k` to the quotient. Handle the single overflow case `MIN / -1` first.

* Time: **O(log² n)** — at most 31 outer rounds, each doubling up to 31 times.
* Space: **O(1)** — a few ints.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0029/v1/DivideTwoIntegers.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0029/v1/DivideTwoIntegersTest.java` | JUnit 6 tests |
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
