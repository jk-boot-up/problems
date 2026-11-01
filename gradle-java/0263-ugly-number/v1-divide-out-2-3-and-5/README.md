# 263. Ugly Number — v1: Divide out 2, 3 and 5

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Math &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/ugly-number/)

## Problem

An **ugly number** is a positive integer whose only prime factors are 2, 3 and 5. Return `true` if `n` is ugly. (1 counts as ugly.)

**Example**
```
6  → true   (2 × 3)
1  → true
14 → false  (has the factor 7)
```

**Constraints**
* `-2^31 <= n <= 2^31 - 1`

## Approach: Divide out 2, 3 and 5

> Divide out every 2, 3 and 5; an ugly number is left with 1.

**Strip the allowed factors.** Non-positive numbers are not ugly. Otherwise divide by 2 while possible, then 3, then 5. Only 1 remains if
no other prime was present.

* Time: **O(log n)** — each division at least halves… or thirds… the number.
* Space: **O(1)**.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0263/v1/UglyNumber.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0263/v1/UglyNumberTest.java` | JUnit 6 tests |
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
