# 1209. Remove All Adjacent Duplicates in String II — v1: Stack of runs

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Stack &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/)

## Problem

Repeatedly remove `k` adjacent equal letters from `s` until no such group remains. Return the final string.

**Example**
```
s = "abcd",                 k = 2 → "abcd"
s = "deeedbbcccbdaa",       k = 3 → "aa"
s = "pbbcggttciiippooaais", k = 2 → "ps"
```

**Constraints**
* `1 <= s.length <= 10^5`, `2 <= k <= 10^4`

## Approach: Stack of runs

> Keep a stack of (letter, run length); when a run reaches k, pop it.

**Runs on a stack.** Push each letter: if it matches the top run, increase that run's count, else push a new run of 1. When a count hits
`k`, pop the run; the runs on either side can now merge naturally on the next push. Rebuild the string from the remaining runs.

* Time: **O(n)**.
* Space: **O(n)**.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p1209/v1/RemoveAdjacentDuplicatesII.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p1209/v1/RemoveAdjacentDuplicatesIITest.java` | JUnit 6 tests |
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
