# 125. Valid Palindrome — v1: Two pointers

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Two Pointers &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/valid-palindrome/)

## Problem

A phrase is a **palindrome** if, after lower-casing it and removing every non-alphanumeric character, it reads the same
forward and backward. Return `true` if `s` is a palindrome.

**Example 1**
```
Input:  s = "A man, a plan, a canal: Panama"
Output: true
```

**Example 2**
```
Input:  s = "race a car"
Output: false
```

**Example 3**
```
Input:  s = " "
Output: true
```

**Constraints**
* `1 <= s.length <= 2 * 10^5`, printable ASCII.

## Approach: Two pointers

> Two pointers move inward, skipping non-alphanumerics and comparing letters case-insensitively.

**Two pointers.** `l` starts at 0 and `r` at the end. Skip characters that are not letters or digits. Compare
`toLowerCase(s[l])` with `toLowerCase(s[r])`; on mismatch return `false`; otherwise move both inward.

* Time: **O(n)** — each character is visited at most once.
* Space: **O(1)** — no cleaned copy of the string.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0125/v1/ValidPalindrome.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0125/v1/ValidPalindromeTest.java` | JUnit 6 tests |
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
