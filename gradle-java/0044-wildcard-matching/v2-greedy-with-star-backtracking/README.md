# 44. Wildcard Matching — v2: Greedy with star backtracking

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

## Approach: Greedy with star backtracking

> Greedy with backtracking to the last '*': let the star absorb one more character whenever a mismatch occurs.

**Greedy.** Walk `i` in `s` and `j` in `p`. On a direct match or `?`, advance both. On `*`, remember its position and the current `i`, and
advance `j` (the star matches nothing for now). On a mismatch after a star, let the star match one more character: `i = ++mark`,
`j = star + 1`. Finally skip trailing stars.

* Time: **O(m·n)** — worst case, though usually close to linear.
* Space: **O(1)** — a few indices.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0044/v2/WildcardMatching.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0044/v2/WildcardMatchingTest.java` | JUnit 6 tests |
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

* [v1-dp-table](../v1-dp-table/README.md): DP table (`O(m·n)` time, `O(m·n)` space)
