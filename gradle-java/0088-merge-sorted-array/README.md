# 88. Merge Sorted Array

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Array / String &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/merge-sorted-array/)

## Problem

You get two integer arrays `nums1` and `nums2`, both sorted in non-decreasing order, plus two counts `m` and `n`.
Only the first `m` values of `nums1` are real; its last `n` slots hold `0` as placeholders. `nums2` holds exactly `n` values.

Merge `nums2` into `nums1` **in place** so that `nums1` becomes one sorted array of length `m + n`. The method returns nothing.

**Example 1**
```
Input:  nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: nums1 = [1,2,2,3,5,6]
```

**Example 2**
```
Input:  nums1 = [0], m = 0, nums2 = [1], n = 1
Output: nums1 = [1]
```

**Constraints**
* `nums1.length == m + n`, `nums2.length == n`
* `0 <= m, n <= 200`, `1 <= m + n <= 200`
* `-10^9 <= nums1[i], nums2[j] <= 10^9`

## Solutions

Each version is a separate Gradle subproject, ordered from the simplest idea to the most efficient one.

| Version | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1](v1/README.md) | Copy and sort | `O((m + n) log(m + n))` | `O(log(m + n))` | [▶ animation](v1/animation/index.html) |
| [v2](v2/README.md) | Three pointers from the back | `O(m + n)` | `O(1)` | [▶ animation](v2/animation/index.html) |

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
