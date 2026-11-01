# 53. Maximum Subarray — v1: Brute force over all starts

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Kadane's Algorithm &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/maximum-subarray/)

## Problem

Given an integer array `nums`, find the contiguous subarray (at least one element) with the largest sum, and return that sum.

**Example 1**
```
Input:  nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6   ([4,-1,2,1])
```

**Example 2**
```
Input:  nums = [-1]
Output: -1
```

**Constraints**
* `1 <= nums.length <= 10^5`; `-10^4 <= nums[i] <= 10^4`

## Approach: Brute force over all starts

> For each start, extend to every end, keeping a running sum.

**All subarrays.** For each start `i`, accumulate `sum` while extending `j` and keep the maximum.

* Time: **O(n²)** — about n²/2 subarrays.
* Space: **O(1)** — a running sum.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0053/v1/MaximumSubarray.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0053/v1/MaximumSubarrayTest.java` | JUnit 6 tests |
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

* [v2-kadane-s-algorithm](../v2-kadane-s-algorithm/README.md): Kadane's algorithm (`O(n)` time, `O(1)` space)
