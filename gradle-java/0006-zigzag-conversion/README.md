# 6. Zigzag Conversion

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

## Solutions

One solution, in subproject `v1`.

| Version | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1](v1/README.md) | Optimal | `O(n)` | `O(n)` | [▶ animation](v1/animation/index.html) |

## Build and test

Only a JDK is needed to start Gradle; JDK 25 is downloaded automatically if it is missing.

```bash
./gradlew test          # every version
./gradlew :v1:test      # one version
```

## Animation

Open `vN/animation/index.html` in a browser. It has three tabs:

* **Problem:** the statement and the key idea.
* **Walkthrough:** pick a scenario and press **Play**. Each step is animated and read aloud by your browser's speech engine
  (untick *Narration* to mute). Keys: space = play/pause, ← / → = step, 1–9 = scenario.
* **Complexity:** time and space cost, plotted against the common growth curves, and compared across versions.

Use the header to switch between Light, Medium and Dark themes and between solution versions.
