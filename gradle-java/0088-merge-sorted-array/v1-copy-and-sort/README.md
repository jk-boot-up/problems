# 88. Merge Sorted Array — v1: Copy and sort

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

## Approach: Copy and sort

> Copy nums2 into the empty tail of nums1, then sort the whole array.

**Copy, then sort.** The last `n` slots of `nums1` are free, so copy `nums2` there and call `Arrays.sort`.
Simple and correct, but it ignores that both inputs are already sorted.

* Time: **O((m + n) log(m + n))** — the sort dominates.
* Space: **O(log(m + n))** — the recursion stack of the sort on primitives.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0088/v1/MergeSortedArray.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0088/v1/MergeSortedArrayTest.java` | JUnit 6 tests |
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

* [v2-three-pointers-from-the-back](../v2-three-pointers-from-the-back/README.md): Three pointers from the back (`O(m + n)` time, `O(1)` space)
