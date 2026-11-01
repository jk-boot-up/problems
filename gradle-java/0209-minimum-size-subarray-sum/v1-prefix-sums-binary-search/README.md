# 209. Minimum Size Subarray Sum — v1: Prefix sums + binary search

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

## Approach: Prefix sums + binary search

> With prefix sums, for each start binary-search the first end whose window sum reaches the target.

**Prefix sums.** `pre[i]` = sum of the first `i` values (increasing, since all values are positive). For each `i`,
binary-search the smallest `j` with `pre[j] - pre[i] >= target`; the window length is `j - i`.

* Time: **O(n log n)** — n binary searches.
* Space: **O(n)** — the prefix-sum array.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0209/v1/MinimumSizeSubarraySum.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0209/v1/MinimumSizeSubarraySumTest.java` | JUnit 6 tests |
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
  engine (untick *Narration* to mute). Keys: space = play/pause, ← / → = step, 1–9 = scenario.
* **Complexity:** time and space cost, plotted against the common growth curves, and compared with the other approaches.

Switch between Light, Medium and Dark themes in the header.

## Other approaches

* [v2-sliding-window](../v2-sliding-window/README.md): Sliding window (`O(n)` time, `O(1)` space)
