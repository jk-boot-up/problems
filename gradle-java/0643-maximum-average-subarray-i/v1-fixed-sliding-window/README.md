# 643. Maximum Average Subarray I — v1: Fixed sliding window

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Sliding Window &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/maximum-average-subarray-i/)

## Problem

Find the contiguous subarray of length `k` with the maximum average and return that average.

**Example**
```
nums = [1,12,-5,-6,50,3], k = 4 → 12.75
```

**Constraints**
* `1 <= k <= n <= 10^5`

## Approach: Fixed sliding window

> Slide a window of size k, adding the new element and dropping the old one.

**Rolling sum.** Sum the first `k` values, then for each step add `nums[i]` and subtract `nums[i - k]`; keep the largest sum.

* Time: **O(n)** — one pass.
* Space: **O(1)** — a running sum.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0643/v1/MaximumAverageSubarray.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0643/v1/MaximumAverageSubarrayTest.java` | JUnit 6 tests |
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
