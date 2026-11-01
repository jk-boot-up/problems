# 72. Edit Distance — v1: 2D DP table

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Multidimensional DP &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/edit-distance/)

## Problem

Return the minimum number of operations (insert a character, delete a character, replace a character) to convert `word1` into `word2`.

**Example**
```
horse → ros:  3  (replace h→r, delete r, delete e)
intention → execution:  5
```

**Constraints**
* `0 <= word1.length, word2.length <= 500`; lowercase letters.

## Approach: 2D DP table

> d[i][j] = edits to turn the first i letters of word1 into the first j letters of word2; each cell takes the cheapest last edit.

**Levenshtein DP.** `d[i][0] = i`, `d[0][j] = j`. If `word1[i-1] == word2[j-1]`, `d[i][j] = d[i-1][j-1]`; otherwise
`1 + min(d[i-1][j-1] (replace), d[i-1][j] (delete), d[i][j-1] (insert))`.

* Time: **O(m·n)** — every cell once.
* Space: **O(m·n)** — the table (one row would also do).

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0072/v1/EditDistance.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0072/v1/EditDistanceTest.java` | JUnit 6 tests |
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
