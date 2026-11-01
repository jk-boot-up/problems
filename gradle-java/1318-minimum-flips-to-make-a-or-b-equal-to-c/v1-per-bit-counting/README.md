# 1318. Minimum Flips to Make a OR b Equal to c — v1: Per-bit counting

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Bit Manipulation &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/minimum-flips-to-make-a-or-b-equal-to-c/)

## Problem

Return the minimum number of single-bit flips in `a` and `b` so that `a | b == c`.

**Example**
```
a = 2, b = 6, c = 5 → 3,   a = 4, b = 2, c = 7 → 1,   a = 1, b = 2, c = 3 → 0
```

**Constraints**
* `1 <= a, b, c <= 10^9`

## Approach: Per-bit counting

> Bit by bit: if c's bit is 1, need one 1 among a and b; if it is 0, every 1 in a and b must be flipped.

**Independent bits.** For each of 31 bits: if `c`'s bit is 1 and both `a`, `b` bits are 0, one flip; if `c`'s bit is 0, flip every 1 bit in `a`
and `b` there.

* Time: **O(1)** — 31 bits.
* Space: **O(1)** — a counter.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p1318/v1/MinimumFlips.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p1318/v1/MinimumFlipsTest.java` | JUnit 6 tests |
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
