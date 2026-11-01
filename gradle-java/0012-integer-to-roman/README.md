# 12. Integer to Roman

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

## Solutions

One solution, in subproject `v1`.

| Version | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1](v1/README.md) | Optimal | `O(1)` | `O(1)` | [▶ animation](v1/animation/index.html) |

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
