# 5. Longest Palindromic Substring — v1: DP table

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Multidimensional DP &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/longest-palindromic-substring/)

## Problem

Return the longest **palindromic substring** of `s`.

**Example**
```
"babad" → "bab" (or "aba"),   "cbbd" → "bb"
```

**Constraints**
* `1 <= s.length <= 1000`; digits and English letters.

## Approach: DP table

> s[i..j] is a palindrome if its ends match and s[i+1..j−1] is a palindrome.

**Interval DP.** `pal[i][j] = s[i] == s[j] && (j - i < 2 || pal[i+1][j-1])`. Fill by increasing length and remember the longest true cell.

* Time: **O(n²)** — every (i, j) pair once.
* Space: **O(n²)** — the boolean table.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0005/v1/LongestPalindromicSubstring.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0005/v1/LongestPalindromicSubstringTest.java` | JUnit 6 tests |
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
* **Complexity:** time and space cost, plotted against the common growth curves, and compared with the other approaches.

Switch between Light, Medium and Dark themes in the header.

## Other approaches

* [v2-expand-around-centre](../v2-expand-around-centre/README.md): Expand around centre (`O(n²)` time, `O(1)` space)
