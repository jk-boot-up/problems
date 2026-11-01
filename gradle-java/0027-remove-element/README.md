# 27. Remove Element

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Array / String &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/remove-element/)

## Problem

Given an integer array `nums` and an integer `val`, remove every occurrence of `val` **in place** and return `k`, the number
of elements that are not equal to `val`. The first `k` slots of `nums` must hold those elements (in any order); what remains after
index `k - 1` does not matter.

**Example 1**
```
Input:  nums = [3,2,2,3], val = 3
Output: 2, nums = [2,2,_,_]
```

**Example 2**
```
Input:  nums = [0,1,2,2,3,0,4,2], val = 2
Output: 5, nums = [0,1,3,0,4,_,_,_]
```

**Constraints**
* `0 <= nums.length <= 100`
* `0 <= nums[i] <= 50`, `0 <= val <= 100`

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
