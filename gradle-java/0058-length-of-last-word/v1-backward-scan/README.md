# 58. Length of Last Word — v1: Backward scan

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Array / String &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/length-of-last-word/)

## Problem

Given a string `s` of words and spaces, return the length of the **last** word. A word is a maximal run of non-space characters.

**Example 1**
```
Input:  s = "Hello World"
Output: 5
```

**Example 2**
```
Input:  s = "   fly me   to   the moon  "
Output: 4
```

**Constraints**
* `1 <= s.length <= 10^4`
* `s` has only English letters and spaces, and at least one word.

## Approach: Backward scan

> Scan from the end: skip trailing spaces, then count letters until the next space.

**Backward scan.** Start at the end, skip spaces, then count characters until a space or the start of the string.

* Time: **O(n)** — at worst we scan the whole string once.
* Space: **O(1)** — an index and a counter.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0058/v1/LengthOfLastWord.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0058/v1/LengthOfLastWordTest.java` | JUnit 6 tests |
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
  engine (untick *Narration* to mute). Keys: space = play/pause, ← / → = step, 1–9 = scenario.
* **Complexity:** time and space cost, plotted against the common growth curves.

Switch between Light, Medium and Dark themes in the header.
