# 132. Palindrome Partitioning II — v1: Centre expansion + cut DP

**Difficulty:** Hard &nbsp;|&nbsp; **Topic:** Multidimensional DP &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/palindrome-partitioning-ii/)

## Problem

Return the minimum number of cuts needed to partition `s` so that every piece is a palindrome.

**Example**
```
"aab" → 1 ("aa" | "b"),   "a" → 0,   "ab" → 1
```

**Constraints**
* `1 <= s.length <= 2000`

## Approach: Centre expansion + cut DP

> Expand around every centre; each palindrome s[l..r] offers cuts[r + 1] = cuts[l] + 1.

**DP on prefix lengths.** `cuts[i]` = minimum pieces for `s[0..i)` minus 1 (`cuts[0] = -1`). For each centre, expand outward; every palindrome
`s[l..r]` gives `cuts[r+1] = min(cuts[r+1], cuts[l] + 1)`.

* Time: **O(n²)** — every palindrome is enumerated once from its centre.
* Space: **O(n)** — the cuts array.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0132/v1/PalindromePartitioningII.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0132/v1/PalindromePartitioningIITest.java` | JUnit 6 tests |
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
