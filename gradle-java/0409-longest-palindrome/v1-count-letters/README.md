# 409. Longest Palindrome — v1: Count letters

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Hash Map &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/longest-palindrome/)

## Problem

Given a string of upper- and lower-case letters, return the length of the longest palindrome that can be **built** from those letters.
Letters are case-sensitive (`"Aa"` is not a palindrome).

**Example**
```
"abccccdd" → 7   ("dccaccd")
"a"        → 1
```

**Constraints**
* `1 <= s.length <= 2000`

## Approach: Count letters

> Use every pair of equal letters, plus one odd letter in the middle if there is any.

**Pairs plus a centre.** Count each letter. A palindrome can use `count / 2 * 2` copies of every letter (mirrored pairs), and one more
letter in the middle if any count is odd.

* Time: **O(n)**.
* Space: **O(1)** — 128 counters.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0409/v1/LongestPalindrome.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0409/v1/LongestPalindromeTest.java` | JUnit 6 tests |
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
