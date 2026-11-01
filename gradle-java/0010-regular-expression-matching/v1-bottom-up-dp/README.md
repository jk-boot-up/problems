# 10. Regular Expression Matching — v1: Bottom-up DP

**Difficulty:** Hard &nbsp;|&nbsp; **Topic:** Multidimensional DP &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/regular-expression-matching/)

## Problem

Implement full-string regular expression matching with `.` (any single character) and `*` (zero or more of the preceding element).

**Example**
```
s = "aa",  p = "a"     → false
s = "aa",  p = "a*"    → true
s = "ab",  p = ".*"    → true
s = "aab", p = "c*a*b" → true
```

**Constraints**
* `1 <= s.length <= 20`; `1 <= p.length <= 20`; every `*` follows a valid character.

## Approach: Bottom-up DP

> dp[i][j]: does s[i..] match p[j..]? A 'x*' either matches nothing or eats one matching character and stays.

**Suffix DP.** `dp[i][j]` is true if `s[i..]` matches `p[j..]`; `dp[m][n] = true`. With `first = i < m && (p[j] == s[i] || p[j] == '.')`:
if `p[j+1] == '*'`, `dp[i][j] = dp[i][j+2] || (first && dp[i+1][j])`; otherwise `dp[i][j] = first && dp[i+1][j+1]`.

* Time: **O(m·n)** — each cell once.
* Space: **O(m·n)** — the table.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0010/v1/RegularExpressionMatching.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0010/v1/RegularExpressionMatchingTest.java` | JUnit 6 tests |
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
