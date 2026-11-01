# 273. Integer to English Words — v1: Three-digit groups

**Difficulty:** Hard &nbsp;|&nbsp; **Topic:** String &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/integer-to-english-words/)

## Problem

Convert a non-negative integer to its English words representation.

**Example**
```
123        → "One Hundred Twenty Three"
12345      → "Twelve Thousand Three Hundred Forty Five"
1234567    → "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
```

**Constraints**
* `0 <= num <= 2^31 - 1`

## Approach: Three-digit groups

> Split into groups of three digits; each group is spelled the same way, followed by Billion, Million or Thousand.

**Groups of three.** From the billions down, take each three-digit chunk. Spell a chunk as `"<d> Hundred"` (if any) plus either a word for
1–19 or a tens word and an optional unit word, then add the group's scale word. Skip empty chunks so `1000010` reads "One Million Ten".
`0` is the only input that says "Zero".

* Time: **O(1)** — at most four groups.
* Space: **O(1)** — the output is bounded.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0273/v1/IntegerToEnglish.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0273/v1/IntegerToEnglishTest.java` | JUnit 6 tests |
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
