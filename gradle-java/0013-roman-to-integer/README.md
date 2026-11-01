# 13. Roman to Integer

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

## Solutions

One solution, in subproject `v1`.

| Version | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1](v1/README.md) | Optimal | `O(n)` | `O(1)` | [▶ animation](v1/animation/index.html) |

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
