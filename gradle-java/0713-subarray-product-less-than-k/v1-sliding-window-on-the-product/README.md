# 713. Subarray Product Less Than K — v1: Sliding window on the product

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Sliding Window &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/subarray-product-less-than-k/)

## Problem

Given positive integers `nums`, return the number of contiguous subarrays whose product is **strictly less** than `k`.

**Example**
```
nums = [10,5,2,6], k = 100 → 8,   nums = [1,2,3], k = 0 → 0
```

**Constraints**
* `1 <= nums.length <= 3 * 10^4`; `1 <= nums[i] <= 1000`; `0 <= k <= 10^6`

## Approach: Sliding window on the product

> Grow the window right, shrink left while the product is too big; every window ending at right contributes its length.

**Window.** Multiply in `nums[right]`; while the product is `>= k`, divide out `nums[left]` and advance. All subarrays ending at `right` and
starting in `[left, right]` are valid: add `right - left + 1`. If `k <= 1`, nothing qualifies.

* Time: **O(n)** — each index enters and leaves once.
* Space: **O(1)** — a product and two indices.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0713/v1/SubarrayProductLessThanK.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0713/v1/SubarrayProductLessThanKTest.java` | JUnit 6 tests |
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
