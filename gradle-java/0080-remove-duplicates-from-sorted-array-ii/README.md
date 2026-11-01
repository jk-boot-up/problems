# 80. Remove Duplicates from Sorted Array II

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Array / String &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/)

## Problem

`nums` is sorted in non-decreasing order. Remove extra duplicates **in place** so that every distinct value appears **at most twice**,
keeping the relative order. Return `k`, the length of the result; the first `k` slots of `nums` must hold it. Use O(1) extra memory.

**Example 1**
```
Input:  nums = [1,1,1,2,2,3]
Output: 5, nums = [1,1,2,2,3,_]
```

**Example 2**
```
Input:  nums = [0,0,1,1,1,1,2,3,3]
Output: 7, nums = [0,0,1,1,2,3,3,_,_]
```

**Constraints**
* `1 <= nums.length <= 3 * 10^4`
* `-10^4 <= nums[i] <= 10^4`, sorted non-decreasing

## Solutions

One solution, in subproject `v1`.

| Version | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1](v1/README.md) | Optimal | `O(n)` | `O(1)` | [▶ animation](v1/animation/index.html) |

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
