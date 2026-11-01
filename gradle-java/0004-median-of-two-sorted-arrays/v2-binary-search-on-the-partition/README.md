# 4. Median of Two Sorted Arrays — v2: Binary search on the partition

**Difficulty:** Hard &nbsp;|&nbsp; **Topic:** Binary Search &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/median-of-two-sorted-arrays/)

## Problem

Given two sorted arrays `nums1` (size `m`) and `nums2` (size `n`), return the **median** of all `m + n` values, in O(log(m + n)).

**Example 1**
```
Input:  nums1 = [1,3], nums2 = [2]
Output: 2.0
```

**Example 2**
```
Input:  nums1 = [1,2], nums2 = [3,4]
Output: 2.5
```

**Constraints**
* `0 <= m, n <= 1000`; `1 <= m + n <= 2000`

## Approach: Binary search on the partition

> Binary-search a cut in the shorter array so that the left halves of both arrays hold exactly the smaller half of all values.

**Partition search.** Make `A` the shorter array. Choose `i` elements from `A` and `j = (m + n + 1) / 2 - i` from `B` for the left half.
The cut is right when `A[i-1] <= B[j]` and `B[j-1] <= A[i]` (missing neighbours count as ±∞). If `A[i-1]` is too big, move `i` left;
otherwise move it right. The median comes from the largest value on the left and the smallest on the right.

* Time: **O(log min(m, n))** — binary search over the shorter array.
* Space: **O(1)** — a few indices.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0004/v2/MedianOfTwoSortedArrays.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0004/v2/MedianOfTwoSortedArraysTest.java` | JUnit 6 tests |
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

* [v1-merge-until-the-middle](../v1-merge-until-the-middle/README.md): Merge until the middle (`O(m + n)` time, `O(1)` space)
