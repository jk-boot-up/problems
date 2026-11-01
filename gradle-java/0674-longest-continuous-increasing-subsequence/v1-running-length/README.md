# 674. Longest Continuous Increasing Subsequence — v1: Running length

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Arrays & Hashing &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/longest-continuous-increasing-subsequence/)

## Problem

Return the length of the longest strictly increasing **contiguous** subarray.

**Example**
```
[1,3,5,4,7] → 3,   [2,2,2,2,2] → 1
```

**Constraints**
* `1 <= nums.length <= 10^4`

## Approach: Running length

> Extend the current strictly increasing run or restart it; keep the longest.

**One pass.** `run = nums[i] > nums[i-1] ? run + 1 : 1`; track the maximum.

* Time: **O(n)** — one pass.
* Space: **O(1)** — two counters.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0674/v1/LongestContinuousIncreasing.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0674/v1/LongestContinuousIncreasingTest.java` | JUnit 6 tests |
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
