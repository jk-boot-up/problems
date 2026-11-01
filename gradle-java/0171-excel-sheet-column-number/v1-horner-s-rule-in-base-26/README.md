# 171. Excel Sheet Column Number — v1: Horner's rule in base 26

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Math &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/excel-sheet-column-number/)

## Problem

Given a column title as shown in a spreadsheet, return its column number (`A → 1`, `Z → 26`, `AA → 27`, …).

**Example**
```
"A"  → 1
"AB" → 28
"ZY" → 701
```

**Constraints**
* `1 <= columnTitle.length <= 7`, upper-case letters, value at most `2^31 - 1`

## Approach: Horner's rule in base 26

> Read the title like a base-26 number whose digits are A = 1 … Z = 26.

**Horner's rule.** Scan left to right: `result = result * 26 + (letter - 'A' + 1)`.

* Time: **O(n)** — one step per letter.
* Space: **O(1)**.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0171/v1/ExcelColumnNumber.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0171/v1/ExcelColumnNumberTest.java` | JUnit 6 tests |
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
