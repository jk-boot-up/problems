# 583. Delete Operation for Two Strings — v1: Longest common subsequence

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Dynamic Programming &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/delete-operation-for-two-strings/)

## Problem

Return the minimum number of single-character deletions (from either string) needed to make `word1` and `word2` equal.

**Example**
```
"sea", "eat"       → 2   (delete 's' and 't')
"leetcode", "etco" → 4
```

**Constraints**
* `1 <= length <= 500`, lower-case letters

## Approach: Longest common subsequence

> Keep the longest common subsequence and delete everything else.

**LCS.** What survives in both strings is a common subsequence; to delete as little as possible, keep the longest one. Compute the LCS
length with the standard table (`dp[i][j] = dp[i-1][j-1] + 1` on a match, else the max of the two neighbours) using one row. Answer:
`m + n - 2 · LCS`.

* Time: **O(mn)**.
* Space: **O(n)** — one row.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0583/v1/DeleteOperationTwoStrings.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0583/v1/DeleteOperationTwoStringsTest.java` | JUnit 6 tests |
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
