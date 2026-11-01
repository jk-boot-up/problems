# 258. Add Digits — v1: Repeated digit sums

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Math &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/add-digits/)

## Problem

Given a non-negative integer `num`, repeatedly add its digits until one digit remains, and return it.

**Example**
```
38 → 3 + 8 = 11 → 1 + 1 = 2
0  → 0
```

**Constraints**
* `0 <= num <= 2^31 - 1`

## Approach: Repeated digit sums

> Literally add the digits until one is left.

**Simulation.** While `num >= 10`, replace it with the sum of its digits.

* Time: **O(log n)** — the first sum reads every digit; later sums are tiny.
* Space: **O(1)**.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0258/v1/AddDigits.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0258/v1/AddDigitsTest.java` | JUnit 6 tests |
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

* [v2-digital-root-formula](../v2-digital-root-formula/README.md): Digital root formula (`O(1)` time, `O(1)` space)
