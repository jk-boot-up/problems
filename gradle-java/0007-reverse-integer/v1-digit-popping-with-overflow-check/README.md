# 7. Reverse Integer — v1: Digit popping with overflow check

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Math &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/reverse-integer/)

## Problem

Reverse the digits of a signed 32-bit integer `x`. If the result overflows the 32-bit range, return 0. Assume no 64-bit integers are
available.

**Example**
```
123 → 321,   -123 → -321,   120 → 21,   1534236469 → 0
```

**Constraints**
* `-2^31 <= x <= 2^31 - 1`

## Approach: Digit popping with overflow check

> Pop digits from the end and push them onto the result, checking for 32-bit overflow before each push.

**Check before multiplying.** `rev * 10 + d` overflows exactly when `rev > MAX/10` (or equals it with `d > 7`), and symmetrically for the
minimum. Java's `%` keeps the sign, so negative numbers work digit by digit.

* Time: **O(log x)** — one step per digit.
* Space: **O(1)** — one int.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0007/v1/ReverseInteger.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0007/v1/ReverseIntegerTest.java` | JUnit 6 tests |
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
