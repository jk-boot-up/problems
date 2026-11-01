# 5. Longest Palindromic Substring — v2: Expand around centre

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Multidimensional DP &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/longest-palindromic-substring/)

## Problem

Return the longest **palindromic substring** of `s`.

**Example**
```
"babad" → "bab" (or "aba"),   "cbbd" → "bb"
```

**Constraints**
* `1 <= s.length <= 1000`; digits and English letters.

## Approach: Expand around centre

> Every palindrome has a centre; grow outward from each of the 2n − 1 centres while the ends match.

**Centres.** A palindrome is centred on a character (odd length) or between two characters (even length). For each of these `2n - 1`
centres, expand `l--, r++` while `s[l] == s[r]` and keep the longest.

* Time: **O(n²)** — each centre can expand up to n/2 times.
* Space: **O(1)** — a few indices.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0005/v2/LongestPalindromicSubstring.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0005/v2/LongestPalindromicSubstringTest.java` | JUnit 6 tests |
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

* [v1-dp-table](../v1-dp-table/README.md): DP table (`O(n²)` time, `O(n²)` space)
