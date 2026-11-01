# 53. Maximum Subarray — v2: Kadane's algorithm

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

## Approach: Kadane's algorithm

> Kadane: the best subarray ending here either extends the previous one or starts fresh at this element.

**Kadane's algorithm.** `cur` = best sum of a subarray ending at `i` = `max(nums[i], cur + nums[i])`: extending only helps if `cur`
is positive. Track the maximum `cur` ever seen.

* Time: **O(n)** — one pass.
* Space: **O(1)** — two numbers.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0053/v2/MaximumSubarray.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0053/v2/MaximumSubarrayTest.java` | JUnit 6 tests |
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

* [v1-brute-force-over-all-starts](../v1-brute-force-over-all-starts/README.md): Brute force over all starts (`O(n²)` time, `O(1)` space)
