# 918. Maximum Sum Circular Subarray — v1: Max and min Kadane

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Kadane's Algorithm &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/maximum-sum-circular-subarray/)

## Problem

`nums` is a **circular** array (the end connects to the start). Return the maximum possible sum of a non-empty subarray, where each
element may be used at most once.

**Example 1**
```
Input:  nums = [5,-3,5]
Output: 10   ([5,5], wrapping around)
```

**Example 2**
```
Input:  nums = [-3,-2,-3]
Output: -2
```

**Constraints**
* `1 <= n <= 3 * 10^4`; `-3 * 10^4 <= nums[i] <= 3 * 10^4`

## Approach: Max and min Kadane

> A wrapping subarray is the total minus a minimum middle subarray; take the better of that and normal Kadane.

**Two Kadanes in one pass.** The best subarray either does not wrap (normal Kadane maximum) or wraps, in which case it is
`total - (minimum subarray)`. If every number is negative, the minimum subarray is the whole array and the wrap formula would give an
empty subarray, so return the normal maximum.

* Time: **O(n)** — one pass.
* Space: **O(1)** — a few running sums.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0918/v1/MaximumCircularSubarray.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0918/v1/MaximumCircularSubarrayTest.java` | JUnit 6 tests |
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
