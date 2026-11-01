# 709. To Lower Case — v1: Character arithmetic

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Strings &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/to-lower-case/)

## Problem

Return `s` with every uppercase letter replaced by its lowercase version.

**Example**
```
"Hello" → "hello",   "LOVELY" → "lovely"
```

**Constraints**
* `1 <= s.length <= 100`; printable ASCII.

## Approach: Character arithmetic

> Upper-case letters A–Z sit exactly 32 code points below their lower-case versions.

**ASCII offset.** For each character in `'A'..'Z'`, add 32 (`'a' - 'A'`); leave others alone.

* Time: **O(n)** — one pass.
* Space: **O(n)** — the result.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0709/v1/ToLowerCase.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0709/v1/ToLowerCaseTest.java` | JUnit 6 tests |
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
