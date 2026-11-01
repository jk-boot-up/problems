# 557. Reverse Words in a String III — v1: Reverse each word

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Two Pointers &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/reverse-words-in-a-string-iii/)

## Problem

Reverse the characters of every word in `s` while keeping the word order and the single spaces.

**Example**
```
"Let's take LeetCode contest" → "s'teL ekat edoCteeL tsetnoc"
```

**Constraints**
* `1 <= s.length <= 5 * 10^4`; words are separated by single spaces.

## Approach: Reverse each word

> Find each word's boundaries and reverse its characters in place.

**Two pointers per word.** Scan for each word's start and end, and swap characters inward.

* Time: **O(n)** — each character is swapped once.
* Space: **O(n)** — the character array.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0557/v1/ReverseWordsIII.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0557/v1/ReverseWordsIIITest.java` | JUnit 6 tests |
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
