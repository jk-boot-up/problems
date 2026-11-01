# 415. Add Strings — v1: Digit-by-digit with carry

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Math &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/add-strings/)

## Problem

Given two non-negative integers as strings, return their sum as a string, without converting the inputs to numbers.

**Example**
```
"11"  + "123" → "134"
"456" + "77"  → "533"
"0"   + "0"   → "0"
```

**Constraints**
* `1 <= length <= 10^4`; no leading zeros except `"0"`

## Approach: Digit-by-digit with carry

> Grade-school addition from the last digit, carrying as you go.

**Column addition.** Walk both strings from the right, adding digits and the carry. A missing digit counts as 0. Keep going while
either string has digits or a carry is left, then reverse the built string.

* Time: **O(max(m, n))**.
* Space: **O(max(m, n))** — the result.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0415/v1/AddStrings.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0415/v1/AddStringsTest.java` | JUnit 6 tests |
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
