# 1438. Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit — v1: Window with max/min deques

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Sliding Window &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/)

## Problem

Return the length of the longest non-empty subarray in which the absolute difference between **any** two elements is at most `limit`
(equivalently, `max - min <= limit`).

**Example**
```
nums = [8,2,4,7],         limit = 4 → 2   ([2,4] or [4,7])
nums = [10,1,2,4,7,2],    limit = 5 → 4   ([2,4,7,2])
nums = [4,2,2,2,4,4,2,2], limit = 0 → 3
```

**Constraints**
* `1 <= nums.length <= 10^5`

## Approach: Window with max/min deques

> Slide a window while two monotonic deques report its current max and min in O(1).

**Two deques.** `maxQ` holds values in decreasing order and `minQ` in increasing order, so their fronts are the window's max and min. Add
`nums[hi]` to both (dropping smaller / larger values from the back). While `max - min > limit`, move `lo` right, removing `nums[lo]` from a
deque front if it is there.

* Time: **O(n)** — every value enters and leaves each deque once.
* Space: **O(n)** — the deques.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p1438/v1/LongestSubarrayWithinLimit.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p1438/v1/LongestSubarrayWithinLimitTest.java` | JUnit 6 tests |
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
