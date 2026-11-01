# 28. Find the Index of the First Occurrence in a String — v2: KMP

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Array / String &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/)

## Problem

Return the index of the first occurrence of `needle` in `haystack`, or `-1` if `needle` does not occur.

**Example 1**
```
Input:  haystack = "sadbutsad", needle = "sad"
Output: 0
```

**Example 2**
```
Input:  haystack = "leetcode", needle = "leeto"
Output: -1
```

**Constraints**
* `1 <= haystack.length, needle.length <= 10^4`, lowercase letters only.

## Approach: KMP

> KMP: precompute how far the needle can fall back on a mismatch, so the haystack pointer never moves backwards.

**Knuth–Morris–Pratt.** Build `lps[i]`: the length of the longest proper prefix of `needle[0..i]` that is also its suffix.
Then scan the haystack with `j` matched characters. On a mismatch, fall back to `j = lps[j-1]` instead of restarting,
so the haystack index only moves forward.

* Time: **O(n + m)** — building lps is O(m), and the scan is O(n).
* Space: **O(m)** — the lps table.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0028/v2/StrStr.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0028/v2/StrStrTest.java` | JUnit 6 tests |
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
  engine (untick *Narration* to mute). Keys: space = play/pause, ← / → = step, 1–9 = scenario.
* **Complexity:** time and space cost, plotted against the common growth curves, and compared with the other approaches.

Switch between Light, Medium and Dark themes in the header.

## Other approaches

* [v1-brute-force](../v1-brute-force/README.md): Brute force (`O(n·m)` time, `O(1)` space)
