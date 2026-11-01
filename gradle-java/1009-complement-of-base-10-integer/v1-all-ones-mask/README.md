# 1009. Complement of Base 10 Integer — v1: All-ones mask

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Bit Manipulation &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/complement-of-base-10-integer/)

## Problem

The complement flips every bit of a number's binary representation (without leading zeros). Return the complement of `n`.

**Example**
```
5 (101) → 2 (010),   7 (111) → 0,   10 (1010) → 5 (0101),   0 → 1
```

**Constraints**
* `0 <= n < 10^9`

## Approach: All-ones mask

> XOR n with a mask of 1s as long as n's binary representation.

**Mask.** Build `mask = 1, 11, 111, …` until it covers `n`; the answer is `n ^ mask` (for `n = 0`, the mask is `1`).

* Time: **O(log n)** — one step per bit.
* Space: **O(1)** — one mask.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p1009/v1/ComplementOfBase10.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p1009/v1/ComplementOfBase10Test.java` | JUnit 6 tests |
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
