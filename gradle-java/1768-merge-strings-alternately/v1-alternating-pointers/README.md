# 1768. Merge Strings Alternately — v1: Alternating pointers

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Two Pointers &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/merge-strings-alternately/)

## Problem

Merge `word1` and `word2` by alternating their letters, starting with `word1`. If one is longer, append its remaining letters.

**Example**
```
"abc", "pqr"  → "apbqcr"
"ab", "pqrs"  → "apbqrs"
```

**Constraints**
* `1 <= word1.length, word2.length <= 100`

## Approach: Alternating pointers

> Take one letter from each string in turn; append whatever is left of the longer one.

**One loop.** For `i` from 0 to the longer length, append `word1[i]` and `word2[i]` when they exist.

* Time: **O(m + n)** — each letter once.
* Space: **O(m + n)** — the result.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p1768/v1/MergeStringsAlternately.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p1768/v1/MergeStringsAlternatelyTest.java` | JUnit 6 tests |
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
