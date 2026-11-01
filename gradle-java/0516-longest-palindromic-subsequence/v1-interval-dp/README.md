# 516. Longest Palindromic Subsequence — v1: Interval DP

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Multidimensional DP &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/longest-palindromic-subsequence/)

## Problem

Return the length of the longest **palindromic subsequence** of `s`.

**Example**
```
"bbbab" → 4 ("bbbb"),   "cbbd" → 2 ("bb")
```

**Constraints**
* `1 <= s.length <= 1000`

## Approach: Interval DP

> Matching ends add 2 to the inner answer; otherwise drop one end.

**Interval DP.** `dp[i][j]` for `s[i..j]`: `dp[i][i] = 1`; equal ends give `dp[i+1][j-1] + 2`; otherwise `max(dp[i+1][j], dp[i][j-1])`.
Fill `i` from right to left.

* Time: **O(n²)** — each interval once.
* Space: **O(n²)** — the table.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0516/v1/LongestPalindromicSubsequence.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0516/v1/LongestPalindromicSubsequenceTest.java` | JUnit 6 tests |
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
