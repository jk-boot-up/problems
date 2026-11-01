# 166. Fraction to Recurring Decimal — v1: Long division with a remainder map

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Hash Map &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/fraction-to-recurring-decimal/)

## Problem

Given two integers `numerator` and `denominator`, return the fraction as a string. If the fractional part repeats, wrap the repeating
part in parentheses.

**Example**
```
1 / 2    → "0.5"
2 / 1    → "2"
4 / 333  → "0.(012)"
1 / 6    → "0.1(6)"
-50 / 8  → "-6.25"
```

**Constraints**
* `-2^31 <= numerator, denominator <= 2^31 - 1`, `denominator != 0`

## Approach: Long division with a remainder map

> Long division repeats exactly when a remainder repeats; remember where each remainder first appeared.

**Long division.** Work with `long` absolute values (so `-2^31` does not overflow) and add the sign first. After the integer part, keep
multiplying the remainder by 10 to produce the next digit. Store each remainder with the position of the digit it produces. When a
remainder comes back, the digits from that position onward repeat forever: insert `(` there and close with `)`.

* Time: **O(d)** — `d` is the denominator; there are fewer than `d` distinct remainders.
* Space: **O(d)** — the remainder map.

Hash lookups use `MyHashMap` / `MyHashSet`, our own hash table (bucket array, chaining, resizing), instead of `java.util.HashMap`.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0166/v1/FractionToDecimal.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0166/v1/FractionToDecimalTest.java` | JUnit 6 tests |
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
