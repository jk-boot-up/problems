# 712. Minimum ASCII Delete Sum for Two Strings — v1: DP over suffixes

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Dynamic Programming &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/minimum-ascii-delete-sum-for-two-strings/)

## Problem

Return the lowest total ASCII value of characters deleted from `s1` and `s2` to make the two strings equal.

**Example**
```
"sea", "eat"      → 231   (delete 's' = 115 and 't' = 116)
"delete", "leet"  → 403
```

**Constraints**
* `1 <= length <= 1000`, lower-case letters

## Approach: DP over suffixes

> Edit-distance style DP where deleting a character costs its ASCII code.

**DP.** `dp[i][j]` is the cost to make the prefixes `s1[0..i)` and `s2[0..j)` equal. Equal last characters cost nothing:
`dp[i-1][j-1]`. Otherwise delete one of them: `min(dp[i-1][j] + s1[i-1], dp[i][j-1] + s2[j-1])`. The first row and column delete
everything.

* Time: **O(mn)**.
* Space: **O(n)** — one row.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0712/v1/MinimumDeleteSum.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0712/v1/MinimumDeleteSumTest.java` | JUnit 6 tests |
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
