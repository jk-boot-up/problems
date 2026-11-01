# 115. Distinct Subsequences — v1: 1D DP

**Difficulty:** Hard &nbsp;|&nbsp; **Topic:** Multidimensional DP &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/distinct-subsequences/)

## Problem

Return the number of distinct **subsequences** of `s` that equal `t` (the answer fits in 32 bits).

**Example**
```
s = "rabbbit", t = "rabbit" → 3
s = "babgbag", t = "bag"    → 5
```

**Constraints**
* `1 <= s.length, t.length <= 1000`

## Approach: 1D DP

> ways[j] = number of ways to form t[..j) from the characters seen so far; a matching character adds ways[j−1].

**Rolling DP.** `ways[0] = 1` (the empty prefix of `t`). For each character `c` of `s`, go through `j` from high to low: if `t[j-1] == c`,
then `ways[j] += ways[j-1]` (use `c` as the j-th character). Going right to left uses each `c` at most once per subsequence.

* Time: **O(m·n)** — every pair of positions.
* Space: **O(n)** — one row (n = t.length).

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0115/v1/DistinctSubsequences.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0115/v1/DistinctSubsequencesTest.java` | JUnit 6 tests |
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
