# 172. Factorial Trailing Zeroes — v1: Count factors of five

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Math &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/factorial-trailing-zeroes/)

## Problem

Return the number of trailing zeroes in `n!`.

**Example**
```
3 → 0 (6),   5 → 1 (120),   0 → 0,   25 → 6
```

**Constraints**
* `0 <= n <= 10^4`

**Follow-up:** logarithmic time.

## Approach: Count factors of five

> Each trailing zero needs a factor 10 = 2 × 5, and 5s are the scarce factor, so count the 5s in n!.

**Legendre's formula for 5.** Multiples of 5 contribute one factor of 5, multiples of 25 another, multiples of 125 another, and so on:
the answer is `n/5 + n/25 + n/125 + …`, computed by repeatedly dividing by 5.

* Time: **O(log n)** — about log₅ n divisions.
* Space: **O(1)** — a counter.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0172/v1/FactorialTrailingZeroes.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0172/v1/FactorialTrailingZeroesTest.java` | JUnit 6 tests |
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
