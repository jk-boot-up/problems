# 2108. Find First Palindromic String in the Array — v1: Two-pointer check per word

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Two Pointers &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/find-first-palindromic-string-in-the-array/)

## Problem

Return the first string in `words` that is a palindrome, or `""` if there is none.

**Example**
```
["abc","car","ada","racecar","cool"] → "ada"
["notapalindrome","racecar"]         → "racecar"
["def","ghi"]                        → ""
```

**Constraints**
* `1 <= words.length <= 100`, `1 <= words[i].length <= 100`

## Approach: Two-pointer check per word

> Check each word with two pointers moving inward; return the first that passes.

**Scan.** For each word, compare characters from both ends moving inward; stop at the first mismatch. Return the first word with none.

* Time: **O(total length)**.
* Space: **O(1)**.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p2108/v1/FirstPalindrome.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p2108/v1/FirstPalindromeTest.java` | JUnit 6 tests |
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
