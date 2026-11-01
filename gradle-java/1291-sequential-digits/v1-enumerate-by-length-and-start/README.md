# 1291. Sequential Digits — v1: Enumerate by length and start

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Enumeration &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/sequential-digits/)

## Problem

A number has **sequential digits** if each digit is one more than the previous (like `1234`). Return all such numbers in `[low, high]`,
sorted.

**Example**
```
low = 100,  high = 300   → [123,234]
low = 1000, high = 13000 → [1234,2345,3456,4567,5678,6789,12345]
```

**Constraints**
* `10 <= low <= high <= 10^9`

## Approach: Enumerate by length and start

> There are only 36 numbers with consecutive increasing digits; generate them in order and keep those in range.

**Enumerate.** Such a number is fixed by its length `L` (2..9) and first digit `s` (1..10-L). Loop over lengths, then starts; within a length
the numbers increase with the start, and longer numbers are bigger, so they come out sorted. Each is a substring of `"123456789"`.

* Time: **O(1)** — 36 candidates.
* Space: **O(1)**.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p1291/v1/SequentialDigits.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p1291/v1/SequentialDigitsTest.java` | JUnit 6 tests |
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
