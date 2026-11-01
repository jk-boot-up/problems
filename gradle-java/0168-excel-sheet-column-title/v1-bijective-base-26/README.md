# 168. Excel Sheet Column Title — v1: Bijective base-26

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Math &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/excel-sheet-column-title/)

## Problem

Given a positive integer `columnNumber`, return its column title as it appears in a spreadsheet: `1 → A`, `26 → Z`, `27 → AA`,
`28 → AB`, …

**Example**
```
1   → "A"
28  → "AB"
701 → "ZY"
```

**Constraints**
* `1 <= columnNumber <= 2^31 - 1`

## Approach: Bijective base-26

> Base 26 with digits 1..26 instead of 0..25, so subtract one before each step.

**Shift then divide.** Titles are base 26 with no zero digit. Subtract 1 so the last letter becomes `(n - 1) % 26` (0 → `A`, 25 → `Z`),
then continue with `(n - 1) / 26`. Letters come out last-first, so reverse at the end.

* Time: **O(log₂₆ n)** — one letter per step.
* Space: **O(1)** — at most 7 letters.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0168/v1/ExcelColumnTitle.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0168/v1/ExcelColumnTitleTest.java` | JUnit 6 tests |
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
