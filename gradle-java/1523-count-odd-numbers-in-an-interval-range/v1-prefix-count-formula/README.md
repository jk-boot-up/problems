# 1523. Count Odd Numbers in an Interval Range — v1: Prefix count formula

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Math &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/count-odd-numbers-in-an-interval-range/)

## Problem

Return how many odd numbers lie in `[low, high]` (inclusive).

**Example**
```
low = 3, high = 7  → 3   (3, 5, 7)
low = 8, high = 10 → 1   (9)
```

**Constraints**
* `0 <= low <= high <= 10^9`

## Approach: Prefix count formula

> There are (x + 1) / 2 odd numbers in [0, x]; subtract the count below low.

**Prefix counts.** The odd numbers in `[0, x]` number `(x + 1) / 2` (integer division), and those in `[0, low - 1]` number `low / 2`. The
difference is the answer.

* Time: **O(1)**.
* Space: **O(1)**.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p1523/v1/CountOddsInRange.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p1523/v1/CountOddsInRangeTest.java` | JUnit 6 tests |
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
