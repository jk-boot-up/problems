# 387. First Unique Character in a String — v1: Counting array

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Arrays & Hashing &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/first-unique-character-in-a-string/)

## Problem

Return the index of the first character of `s` that does not repeat, or `-1`.

**Example**
```
"leetcode" → 0,   "loveleetcode" → 2,   "aabb" → -1
```

**Constraints**
* `1 <= s.length <= 10^5`; lowercase letters.

## Approach: Counting array

> Count every letter, then return the first index whose letter has count 1.

**Two passes.** Count letters in an `int[26]`, then scan for the first letter with count 1.

* Time: **O(n)** — two passes.
* Space: **O(1)** — 26 counters.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0387/v1/FirstUniqueCharacter.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0387/v1/FirstUniqueCharacterTest.java` | JUnit 6 tests |
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
