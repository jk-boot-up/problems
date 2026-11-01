# 8. String to Integer (atoi) — v1: Single pass with clamping

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Strings &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/string-to-integer-atoi/)

## Problem

Convert a string to a 32-bit signed integer:
1. skip leading spaces; 2. read an optional `+` or `-`; 3. read digits until a non-digit (ignore the rest);
4. if no digits were read the result is 0; 5. clamp to `[-2^31, 2^31 - 1]`.

**Example**
```
"42" → 42,   "   -042" → -42,   "1337c0d3" → 1337,   "0-1" → 0,   "words and 987" → 0
```

**Constraints**
* `0 <= s.length <= 200`

## Approach: Single pass with clamping

> Skip spaces, read an optional sign, then digits, clamping to the 32-bit range as soon as it would overflow.

**Careful scanning.** Accumulate digits; before `result * 10 + d`, check `result > (MAX - d) / 10` and clamp according to the sign.

* Time: **O(n)** — one pass.
* Space: **O(1)** — a few variables.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0008/v1/StringToInteger.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0008/v1/StringToIntegerTest.java` | JUnit 6 tests |
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
