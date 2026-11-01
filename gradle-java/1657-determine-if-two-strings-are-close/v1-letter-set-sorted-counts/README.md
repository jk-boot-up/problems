# 1657. Determine if Two Strings Are Close — v1: Letter set + sorted counts

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Arrays & Hashing &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/determine-if-two-strings-are-close/)

## Problem

Two strings are **close** if one can become the other using (1) swaps of any two characters and (2) transforming every occurrence of one
existing letter into another existing letter and vice versa. Return `true` if `word1` and `word2` are close.

**Example**
```
"abc", "bca" → true,   "a", "aa" → false,   "cabbba", "abbccc" → true
```

**Constraints**
* `1 <= length <= 10^5`; lowercase letters.

## Approach: Letter set + sorted counts

> Swaps and letter-relabelling preserve the set of letters and the multiset of counts; those two must match.

**Invariants.** Swaps keep counts per letter; relabelling permutes counts among existing letters. So the strings are close iff they use the
same set of letters and their sorted count lists are equal.

* Time: **O(n)** — counting (sorting 26 counts is constant).
* Space: **O(1)** — two arrays of 26.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p1657/v1/CloseStrings.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p1657/v1/CloseStringsTest.java` | JUnit 6 tests |
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
