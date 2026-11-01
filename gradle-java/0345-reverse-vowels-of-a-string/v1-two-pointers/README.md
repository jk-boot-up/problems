# 345. Reverse Vowels of a String — v1: Two pointers

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Two Pointers &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/reverse-vowels-of-a-string/)

## Problem

Reverse only the vowels (`a, e, i, o, u` in either case) of `s`.

**Example**
```
"IceCreAm" → "AceCreIm",   "leetcode" → "leotcede"
```

**Constraints**
* `1 <= s.length <= 3 * 10^5`; printable ASCII.

## Approach: Two pointers

> Two pointers move inward, skipping consonants, and swap each pair of vowels they stop on.

**Swap vowels from both ends.** Move `l` right and `r` left until each points at a vowel, swap, repeat.

* Time: **O(n)** — each character is visited once.
* Space: **O(n)** — the character array.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0345/v1/ReverseVowels.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0345/v1/ReverseVowelsTest.java` | JUnit 6 tests |
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
