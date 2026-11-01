# 374. Guess Number Higher or Lower — v1: Binary search on the hint

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Binary Search &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/guess-number-higher-or-lower/)

## Problem

A number `pick` is chosen from `1..n`. The API `guess(num)` returns `-1` if `num > pick`, `1` if `num < pick`, `0` if correct. Return `pick`.
(Here the API is a method of the same class, initialised with the hidden pick.)

**Example**
```
n = 10, pick = 6 → 6,   n = 1, pick = 1 → 1
```

**Constraints**
* `1 <= pick <= n <= 2^31 - 1`

## Approach: Binary search on the hint

> Binary search guided by the hint: too high, too low, or correct.

**Binary search.** Halve `[lo, hi]` according to `guess(mid)`, using `>>>` so `lo + hi` never overflows.

* Time: **O(log n)** — about 31 guesses at most.
* Space: **O(1)** — two bounds.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0374/v1/GuessNumber.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0374/v1/GuessNumberTest.java` | JUnit 6 tests |
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
