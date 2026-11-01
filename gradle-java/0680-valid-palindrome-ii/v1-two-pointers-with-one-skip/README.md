# 680. Valid Palindrome II — v1: Two pointers with one skip

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Two Pointers &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/valid-palindrome-ii/)

## Problem

Return `true` if `s` can be a palindrome after deleting **at most one** character.

**Example**
```
"aba" → true,   "abca" → true (delete 'c'),   "abc" → false
```

**Constraints**
* `1 <= s.length <= 10^5`

## Approach: Two pointers with one skip

> Compare from both ends; at the first mismatch, try skipping either the left or the right character.

**One chance.** Move inward while the ends match. At the first mismatch, the answer is whether `s[l+1..r]` or `s[l..r-1]` is a palindrome.

* Time: **O(n)** — at most two extra linear checks.
* Space: **O(1)** — indices only.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0680/v1/ValidPalindromeII.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0680/v1/ValidPalindromeIITest.java` | JUnit 6 tests |
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
