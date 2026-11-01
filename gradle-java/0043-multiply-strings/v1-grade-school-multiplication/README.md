# 43. Multiply Strings — v1: Grade-school multiplication

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Math &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/multiply-strings/)

## Problem

Multiply two non-negative integers given as strings and return the product as a string, without converting the inputs to integers.

**Example**
```
"2" × "3" = "6",   "123" × "456" = "56088"
```

**Constraints**
* `1 <= num1.length, num2.length <= 200`; no leading zeros except "0".

## Approach: Grade-school multiplication

> Digit i of num1 times digit j of num2 lands at positions i + j and i + j + 1 of the product.

**Position array.** The product has at most `m + n` digits. For every pair of digits, add their product at `i + j + 1` and carry into
`i + j`. Finally skip leading zeros.

* Time: **O(m·n)** — every digit pair.
* Space: **O(m + n)** — the result digits.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0043/v1/MultiplyStrings.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0043/v1/MultiplyStringsTest.java` | JUnit 6 tests |
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
