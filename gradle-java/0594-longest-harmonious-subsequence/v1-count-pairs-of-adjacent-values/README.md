# 594. Longest Harmonious Subsequence — v1: Count pairs of adjacent values

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Arrays & Hashing &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/longest-harmonious-subsequence/)

## Problem

A **harmonious** array has a difference of exactly 1 between its maximum and minimum. Return the length of the longest harmonious
subsequence of `nums`.

**Example**
```
[1,3,2,2,5,2,3,7] → 5 ([3,2,2,2,3]),   [1,2,3,4] → 2,   [1,1,1,1] → 0
```

**Constraints**
* `1 <= nums.length <= 2 * 10^4`

## Approach: Count pairs of adjacent values

> A harmonious subsequence uses only two values x and x + 1; count values and try every x.

**Counting.** Count each value in a `MyHashMap`. For each value `x` that also has `x + 1`, the subsequence of all `x` and `x + 1` has length
`count[x] + count[x+1]`.

* Time: **O(n)** — counting and one pass over the keys.
* Space: **O(n)** — the map.

Hash lookups use `MyHashMap` / `MyHashSet`, our own hash table (bucket array, chaining, resizing), instead of `java.util.HashMap`.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0594/v1/LongestHarmoniousSubsequence.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0594/v1/LongestHarmoniousSubsequenceTest.java` | JUnit 6 tests |
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
