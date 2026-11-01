# 152. Maximum Product Subarray — v1: Max and min running products

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** 1D DP &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/maximum-product-subarray/)

## Problem

Return the largest product of a contiguous non-empty subarray of `nums` (it fits in 32 bits).

**Example**
```
[2,3,-2,4] → 6,   [-2,0,-1] → 0,   [-2,3,-4] → 24
```

**Constraints**
* `1 <= nums.length <= 2 * 10^4`; `-10 <= nums[i] <= 10`

## Approach: Max and min running products

> Track both the largest and smallest product ending here: a negative number swaps their roles.

**Kadane with two values.** `hi` and `lo` are the largest and smallest products of a subarray ending at `i`. For a negative `x`, swap
them first. Then `hi = max(x, hi·x)`, `lo = min(x, lo·x)`, and track the best `hi`.

* Time: **O(n)** — one pass.
* Space: **O(1)** — three numbers.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0152/v1/MaximumProductSubarray.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0152/v1/MaximumProductSubarrayTest.java` | JUnit 6 tests |
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
