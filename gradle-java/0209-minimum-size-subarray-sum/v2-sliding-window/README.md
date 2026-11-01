# 209. Minimum Size Subarray Sum — v2: Sliding window

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Sliding Window &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/minimum-size-subarray-sum/)

## Problem

Given positive integers `nums` and a positive `target`, return the minimal length of a contiguous subarray whose sum is
**at least** `target`. Return `0` if no such subarray exists.

**Example 1**
```
Input:  target = 7, nums = [2,3,1,2,4,3]
Output: 2   ([4,3])
```

**Example 2**
```
Input:  target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0
```

**Constraints**
* `1 <= target <= 10^9`
* `1 <= nums.length <= 10^5`, `1 <= nums[i] <= 10^4`

## Approach: Sliding window

> Grow the window to the right until the sum reaches the target, then shrink it from the left while it still does.

**Sliding window.** Extend `right` and add `nums[right]` to `sum`. While `sum >= target`, record the window length and remove
`nums[left]`, moving `left` forward. All values are positive, so shrinking always lowers the sum.

* Time: **O(n)** — each index enters and leaves the window at most once.
* Space: **O(1)** — the window bounds and the running sum.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0209/v2/MinimumSizeSubarraySum.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0209/v2/MinimumSizeSubarraySumTest.java` | JUnit 6 tests |
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

* [v1-prefix-sums-binary-search](../v1-prefix-sums-binary-search/README.md): Prefix sums + binary search (`O(n log n)` time, `O(n)` space)
