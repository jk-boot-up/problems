# 9. Palindrome Number — v1: Compare as a string

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Math &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/palindrome-number/)

## Problem

Return `true` if the integer `x` reads the same forward and backward.

**Example**
```
121 → true,   -121 → false (reads 121-),   10 → false
```

**Constraints**
* `-2^31 <= x <= 2^31 - 1`

**Follow-up:** solve it without converting to a string.

## Approach: Compare as a string

> Convert to a string and compare characters from both ends.

**String two pointers.** `String.valueOf(x)`, then compare `s[i]` with `s[n-1-i]`.

* Time: **O(log n)** — the string has about log₁₀ n characters.
* Space: **O(log n)** — the string.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0009/v1/PalindromeNumber.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0009/v1/PalindromeNumberTest.java` | JUnit 6 tests |
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

* [v2-reverse-half-the-digits](../v2-reverse-half-the-digits/README.md): Reverse half the digits (`O(log n)` time, `O(1)` space)
