# 91. Decode Ways — v1: Two rolling variables

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** 1D DP &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/decode-ways/)

## Problem

Letters map to numbers `A=1 … Z=26`. Given a digit string `s`, return how many ways it can be decoded. `"06"` is not valid (no leading zeros).

**Example**
```
"12" → 2 ("AB", "L"),   "226" → 3,   "06" → 0
```

**Constraints**
* `1 <= s.length <= 100`; digits only.

## Approach: Two rolling variables

> ways(i) = ways(i−1) if the last digit is 1–9, plus ways(i−2) if the last two digits form 10–26.

**Fibonacci-like DP.** `cur = (one-digit valid ? prev1 : 0) + (two-digit 10..26 ? prev2 : 0)`, shifting the two previous counts forward.

* Time: **O(n)** — one pass.
* Space: **O(1)** — two counts.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0091/v1/DecodeWays.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0091/v1/DecodeWaysTest.java` | JUnit 6 tests |
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
