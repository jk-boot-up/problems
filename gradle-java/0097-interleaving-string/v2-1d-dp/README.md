# 97. Interleaving String — v2: 1D DP

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Multidimensional DP &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/interleaving-string/)

## Problem

Return `true` if `s3` is formed by **interleaving** `s1` and `s2`: splitting both into pieces and alternating them, keeping each
string's characters in order.

**Example**
```
s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac" → true
s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc" → false
s1 = "",      s2 = "",      s3 = ""           → true
```

**Constraints**
* `0 <= s1.length, s2.length <= 100`; `0 <= s3.length <= 200`

**Follow-up:** O(s2.length) extra memory.

## Approach: 1D DP

> ok[i][j]: the first i chars of s1 and j chars of s2 can form the first i + j chars of s3.

**Grid of prefixes.** `ok[i][j]` is true when `s3[0..i+j)` interleaves `s1[0..i)` and `s2[0..j)`: either `ok[i-1][j]` and
`s1[i-1] == s3[i+j-1]`, or `ok[i][j-1]` and `s2[j-1] == s3[i+j-1]`. Keep one row of the grid.

* Time: **O(m·n)** — every cell once.
* Space: **O(n)** — one row (n = s2.length).

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0097/v2/InterleavingString.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0097/v2/InterleavingStringTest.java` | JUnit 6 tests |
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
* **Complexity:** time and space cost, plotted against the common growth curves, and compared with the other approaches.

Switch between Light, Medium and Dark themes in the header.

## Other approaches

* [v1-2d-dp-table](../v1-2d-dp-table/README.md): 2D DP table (`O(m·n)` time, `O(m·n)` space)
