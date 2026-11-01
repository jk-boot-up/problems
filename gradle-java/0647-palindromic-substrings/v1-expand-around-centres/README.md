# 647. Palindromic Substrings — v1: Expand around centres

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Two Pointers &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/palindromic-substrings/)

## Problem

Return how many substrings of `s` are palindromes (substrings at different positions count separately).

**Example**
```
"abc" → 3,   "aaa" → 6
```

**Constraints**
* `1 <= s.length <= 1000`

## Approach: Expand around centres

> Expand around each of the 2n − 1 centres and count every successful expansion.

**Centres.** For each centre (a character or the gap between two), expand while the ends match; every step of the expansion is one more
palindrome.

* Time: **O(n²)** — each centre expands at most n/2 times.
* Space: **O(1)** — a few indices.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0647/v1/PalindromicSubstrings.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0647/v1/PalindromicSubstringsTest.java` | JUnit 6 tests |
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
