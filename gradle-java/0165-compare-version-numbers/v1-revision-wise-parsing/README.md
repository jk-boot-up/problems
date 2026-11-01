# 165. Compare Version Numbers — v1: Revision-wise parsing

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Two Pointers &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/compare-version-numbers/)

## Problem

Compare two version strings made of revisions separated by dots. Revisions compare as integers (leading zeros ignored); a missing revision
counts as 0. Return `-1`, `0` or `1`.

**Example**
```
"1.2", "1.10" → -1,   "1.01", "1.001" → 0,   "1.0", "1.0.0.0" → 0
```

**Constraints**
* `1 <= length <= 500`; revisions fit in 32 bits.

## Approach: Revision-wise parsing

> Compare revision by revision as integers, treating missing revisions as 0.

**Two pointers.** Parse the next revision of each string digit by digit (0 if exhausted) and compare; continue while either string has
characters left.

* Time: **O(m + n)** — each character once.
* Space: **O(1)** — no splitting.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0165/v1/CompareVersionNumbers.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0165/v1/CompareVersionNumbersTest.java` | JUnit 6 tests |
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
