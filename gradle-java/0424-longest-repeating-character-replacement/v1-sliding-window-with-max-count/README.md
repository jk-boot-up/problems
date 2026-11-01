# 424. Longest Repeating Character Replacement — v1: Sliding window with max count

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Sliding Window &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/longest-repeating-character-replacement/)

## Problem

You may change at most `k` characters of `s` (uppercase letters). Return the length of the longest substring containing a single
repeated letter after the changes.

**Example**
```
s = "ABAB", k = 2 → 4,   s = "AABABBA", k = 1 → 4
```

**Constraints**
* `1 <= s.length <= 10^5`; `0 <= k <= s.length`

## Approach: Sliding window with max count

> A window is fixable if its length minus its most frequent letter count is at most k.

**Window that never shrinks.** Track letter counts and `maxCount` (the highest count seen in any window). If
`windowLength - maxCount > k`, move the left edge by one. `maxCount` never needs to decrease: only a larger `maxCount` can produce a longer
valid window, so the window size only grows when the answer grows.

* Time: **O(n)** — each index enters and leaves once.
* Space: **O(1)** — 26 counters.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0424/v1/LongestRepeatingReplacement.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0424/v1/LongestRepeatingReplacementTest.java` | JUnit 6 tests |
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
