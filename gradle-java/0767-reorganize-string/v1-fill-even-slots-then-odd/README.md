# 767. Reorganize String — v1: Fill even slots, then odd

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Greedy &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/reorganize-string/)

## Problem

Rearrange `s` so that no two adjacent characters are equal. Return any valid arrangement, or `""` if none exists.

**Example**
```
"aab"  → "aba"
"aaab" → ""
```

**Constraints**
* `1 <= s.length <= 500`, lower-case letters

## Approach: Fill even slots, then odd

> Place the most frequent letter on the even positions first, then fill the remaining slots in order.

**Even slots first.** If some letter appears more than `(n + 1) / 2` times it is impossible. Otherwise write the most frequent letter at
positions `0, 2, 4, …`, then continue with every other letter, wrapping from the even positions to `1, 3, 5, …`. Equal letters are written
two apart, and the only way a letter could meet itself after the wrap is ruled out because the most frequent letter went first.

* Time: **O(n)**.
* Space: **O(n)** — the output (26 counters otherwise).

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0767/v1/ReorganizeString.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0767/v1/ReorganizeStringTest.java` | JUnit 6 tests |
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
