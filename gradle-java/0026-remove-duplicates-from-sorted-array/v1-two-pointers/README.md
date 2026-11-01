# 26. Remove Duplicates from Sorted Array — v1: Two pointers

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Array / String &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/remove-duplicates-from-sorted-array/)

## Problem

`nums` is sorted in non-decreasing order. Remove the duplicates **in place** so each distinct value appears once, keeping
their relative order. Return `k`, the number of distinct values; the first `k` slots of `nums` must hold them.

**Example 1**
```
Input:  nums = [1,1,2]
Output: 2, nums = [1,2,_]
```

**Example 2**
```
Input:  nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
```

**Constraints**
* `1 <= nums.length <= 3 * 10^4`
* `-100 <= nums[i] <= 100`, sorted non-decreasing

## Approach: Two pointers

> In a sorted array, a value is new exactly when it differs from the last value we kept.

**Two pointers.** `k` is the length of the unique prefix (starts at 1). For each `i` from 1, if `nums[i] != nums[k-1]` it is a
new value, so write it to `nums[k]` and grow `k`.

* Time: **O(n)** — each element is looked at once.
* Space: **O(1)** — duplicates are overwritten in place.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0026/v1/RemoveDuplicates.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0026/v1/RemoveDuplicatesTest.java` | JUnit 6 tests |
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
* **Complexity:** time and space cost, plotted against the common growth curves.

Switch between Light, Medium and Dark themes in the header.
