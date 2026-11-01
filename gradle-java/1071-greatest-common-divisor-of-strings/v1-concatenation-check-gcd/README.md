# 1071. Greatest Common Divisor of Strings — v1: Concatenation check + gcd

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Math &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/greatest-common-divisor-of-strings/)

## Problem

`t` divides `s` if `s` is `t` repeated some number of times. Return the largest string that divides both `str1` and `str2`, or `""`.

**Example**
```
"ABCABC", "ABC" → "ABC",   "ABABAB", "ABAB" → "AB",   "LEET", "CODE" → ""
```

**Constraints**
* `1 <= str1.length, str2.length <= 1000`; uppercase letters.

## Approach: Concatenation check + gcd

> A common divisor exists only if s + t == t + s; then its length is gcd(|s|, |t|).

**Commuting strings.** If both are repetitions of some base `x`, then `str1 + str2` and `str2 + str1` are the same string; the converse
also holds. In that case the largest base has length `gcd(|str1|, |str2|)`.

* Time: **O(m + n)** — one concatenation comparison plus a gcd.
* Space: **O(m + n)** — the concatenations.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p1071/v1/GcdOfStrings.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p1071/v1/GcdOfStringsTest.java` | JUnit 6 tests |
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
