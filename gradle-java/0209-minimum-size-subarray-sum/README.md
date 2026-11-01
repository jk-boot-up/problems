# 209. Minimum Size Subarray Sum

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

## Solutions

Each version is a separate Gradle subproject, ordered from the simplest idea to the most efficient one.

| Version | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1](v1/README.md) | Prefix sums + binary search | `O(n log n)` | `O(n)` | [▶ animation](v1/animation/index.html) |
| [v2](v2/README.md) | Sliding window | `O(n)` | `O(1)` | [▶ animation](v2/animation/index.html) |

## Build and test

Only a JDK is needed to start Gradle; JDK 25 is downloaded automatically if it is missing.

```bash
./gradlew test          # every version
./gradlew :v1:test      # one version
```

## Animation

Open `vN/animation/index.html` in a browser. It has three tabs:

* **Problem:** the statement and the key idea.
* **Walkthrough:** pick a scenario and press **Play**. Each step is animated and read aloud by your browser's speech engine
  (untick *Narration* to mute). Keys: space = play/pause, ← / → = step, 1–9 = scenario.
* **Complexity:** time and space cost, plotted against the common growth curves, and compared across versions.

Use the header to switch between Light, Medium and Dark themes and between solution versions.
