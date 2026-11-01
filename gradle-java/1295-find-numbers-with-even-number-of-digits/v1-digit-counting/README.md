# 1295. Find Numbers with Even Number of Digits — v1: Digit counting

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Math &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/find-numbers-with-even-number-of-digits/)

## Problem

Return how many numbers in `nums` have an even number of digits.

**Example**
```
[12,345,2,6,7896] → 2,   [555,901,482,1771] → 1
```

**Constraints**
* `1 <= nums[i] <= 10^5`

## Approach: Digit counting

> Count each number's digits by repeated division by 10.

**Divide by 10.** Count digits for each number and check parity.

* Time: **O(n log M)** — M is the largest value.
* Space: **O(1)** — counters.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p1295/v1/EvenNumberOfDigits.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p1295/v1/EvenNumberOfDigitsTest.java` | JUnit 6 tests |
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
