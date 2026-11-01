# 6. Zigzag Conversion — v1: Row simulation

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Array / String &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/zigzag-conversion/)

## Problem

Write the string `s` in a zigzag pattern on `numRows` rows (down the rows, then diagonally back up, and repeat), then read it
row by row. For `"PAYPALISHIRING"` with 3 rows:
```
P   A   H   N
A P L S I I G
Y   I   R
```
which reads `"PAHNAPLSIIGYIR"`.

**Example 1**
```
Input:  s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
```

**Example 2**
```
Input:  s = "A", numRows = 1
Output: "A"
```

**Constraints**
* `1 <= s.length <= 1000`, `1 <= numRows <= 1000`

## Approach: Row simulation

> Deal characters onto rows, bouncing the row index down and up; then read the rows in order.

**Simulate the rows.** Keep one `StringBuilder` per row and a current row with a direction. Append each character to the
current row; flip direction at the top and bottom rows. Concatenate the rows. With one row, return `s`.

* Time: **O(n)** — each character is placed once and read once.
* Space: **O(n)** — the row builders hold every character.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0006/v1/ZigzagConversion.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0006/v1/ZigzagConversionTest.java` | JUnit 6 tests |
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
