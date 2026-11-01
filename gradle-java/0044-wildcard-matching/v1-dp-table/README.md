# 44. Wildcard Matching — v1: DP table

**Difficulty:** Hard &nbsp;|&nbsp; **Topic:** Multidimensional DP &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/wildcard-matching/)

## Problem

Implement full-string wildcard matching where `?` matches any single character and `*` matches any sequence (including empty).

**Example**
```
s = "aa", p = "a"    → false
s = "aa", p = "*"    → true
s = "cb", p = "?a"   → false
s = "adceb", p = "*a*b" → true
```

**Constraints**
* `0 <= s.length, p.length <= 2000`

## Approach: DP table

> dp[i][j]: does s[..i) match p[..j)? A star either matches nothing (left) or one more character (up).

**Prefix DP.** `dp[0][0] = true`; leading stars match the empty string. For a star, `dp[i][j] = dp[i][j-1] || dp[i-1][j]`;
for `?` or an equal letter, `dp[i][j] = dp[i-1][j-1]`.

* Time: **O(m·n)** — each cell once.
* Space: **O(m·n)** — the table.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0044/v1/WildcardMatching.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0044/v1/WildcardMatchingTest.java` | JUnit 6 tests |
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

* [v2-greedy-with-star-backtracking](../v2-greedy-with-star-backtracking/README.md): Greedy with star backtracking (`O(m·n)` time, `O(1)` space)
