# 12. Integer to Roman — v1: Greedy value table

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Array / String &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/integer-to-roman/)

## Problem

Convert an integer `num` (1 to 3999) to a Roman numeral. Use the standard symbols `I, V, X, L, C, D, M` and the
subtractive forms `IV, IX, XL, XC, CD, CM`. `I`, `X`, `C` and `M` may repeat up to three times in a row; `V`, `L` and `D` never repeat.

**Example 1**
```
Input:  num = 3749
Output: "MMMDCCXLIX"
```

**Example 2**
```
Input:  num = 58
Output: "LVIII"
```

**Constraints**
* `1 <= num <= 3999`

## Approach: Greedy value table

> Greedy: repeatedly take the largest value (including the six subtractive pairs) that still fits.

**Greedy table.** Use a table of 13 values in descending order: `1000 M, 900 CM, 500 D, 400 CD, 100 C, 90 XC, 50 L, 40 XL, 10 X, 9 IX, 5 V, 4 IV, 1 I`.
While `num` is at least the current value, append its symbol and subtract.

* Time: **O(1)** — the output is at most 15 symbols, because num ≤ 3999.
* Space: **O(1)** — the fixed table and the output builder.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0012/v1/IntegerToRoman.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0012/v1/IntegerToRomanTest.java` | JUnit 6 tests |
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
