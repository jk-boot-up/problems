# 1143. Longest Common Subsequence — v1: 2D DP table

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Multidimensional DP &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/longest-common-subsequence/)

## Problem

Return the length of the longest **common subsequence** of `text1` and `text2` (0 if none).

**Example**
```
"abcde", "ace" → 3,   "abc", "abc" → 3,   "abc", "def" → 0
```

**Constraints**
* `1 <= text1.length, text2.length <= 1000`

## Approach: 2D DP table

> If the last letters match they extend the LCS of the shorter prefixes; otherwise drop one letter from either string.

**Prefix DP.** `dp[i][j]` is the LCS of `text1[..i)` and `text2[..j)`. Equal last letters: `dp[i-1][j-1] + 1`; otherwise
`max(dp[i-1][j], dp[i][j-1])`.

* Time: **O(m·n)** — each cell once.
* Space: **O(m·n)** — the table.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p1143/v1/LongestCommonSubsequence.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p1143/v1/LongestCommonSubsequenceTest.java` | JUnit 6 tests |
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
