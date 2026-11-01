# 238. Product of Array Except Self

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Array / String &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/product-of-array-except-self/)

## Problem

Given an integer array `nums`, return an array `answer` where `answer[i]` equals the product of every element of `nums`
**except** `nums[i]`. Do it in O(n) time **without using division**. Every prefix/suffix product fits in a 32-bit integer.

**Example 1**
```
Input:  nums = [1,2,3,4]
Output: [24,12,8,6]
```

**Example 2**
```
Input:  nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
```

**Constraints**
* `2 <= nums.length <= 10^5`
* `-30 <= nums[i] <= 30`

**Follow-up:** O(1) extra space (the output array does not count).

## Solutions

Each version is a separate Gradle subproject, ordered from the simplest idea to the most efficient one.

| Version | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1](v1/README.md) | Prefix and suffix arrays | `O(n)` | `O(n)` | [▶ animation](v1/animation/index.html) |
| [v2](v2/README.md) | Output array + running suffix | `O(n)` | `O(1)` | [▶ animation](v2/animation/index.html) |

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
