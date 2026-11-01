# 13. Roman to Integer — v1: Look one ahead

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Array / String &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/roman-to-integer/)

## Problem

Roman numerals use `I=1, V=5, X=10, L=50, C=100, D=500, M=1000`. Symbols are usually written largest to smallest,
except for six subtractive pairs: `IV=4, IX=9, XL=40, XC=90, CD=400, CM=900`. Convert a valid Roman numeral `s` to an integer.

**Example 1**
```
Input:  s = "LVIII"
Output: 58
```

**Example 2**
```
Input:  s = "MCMXCIV"
Output: 1994   (M + CM + XC + IV)
```

**Constraints**
* `1 <= s.length <= 15`
* `s` is a valid Roman numeral in the range `[1, 3999]`.

## Approach: Look one ahead

> Add each symbol's value, but subtract it when a larger symbol follows (IV, IX, XL, ...).

**Look one ahead.** For each symbol, if the next symbol is larger, this one is subtracted; otherwise it is added.

* Time: **O(n)** — one pass over the string.
* Space: **O(1)** — a fixed symbol table.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0013/v1/RomanToInteger.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0013/v1/RomanToIntegerTest.java` | JUnit 6 tests |
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
  engine (untick *Narration* to mute). Keys: space = play/pause, ← / → = step, 1–9 = scenario.
* **Complexity:** time and space cost, plotted against the common growth curves.

Switch between Light, Medium and Dark themes in the header.
