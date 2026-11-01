# 451. Sort Characters By Frequency — v1: Bucket sort by count

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Sorting &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/sort-characters-by-frequency/)

## Problem

Sort a string so that characters appearing more often come first; equal characters stay together. Among characters with the same count,
this project lists them in character-code order.

**Example**
```
"tree"   → "eert"
"cccaaa" → "aaaccc"
"Aabb"   → "bbAa"
```

**Constraints**
* `1 <= s.length <= 5 * 10^5`; letters and digits

## Approach: Bucket sort by count

> Count the characters, then bucket them by count and read the buckets from high to low.

**Buckets.** Count every character (128 counters). Counts are at most `n`, so put each character in bucket `count`. Walk the buckets
from `n` down to 1 and write each character `count` times.

* Time: **O(n)** — counting, plus `n + 128` bucket work.
* Space: **O(n)** — the buckets and output.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0451/v1/FrequencySort.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0451/v1/FrequencySortTest.java` | JUnit 6 tests |
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
