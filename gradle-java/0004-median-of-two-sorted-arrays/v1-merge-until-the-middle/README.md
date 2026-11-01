# 4. Median of Two Sorted Arrays — v1: Merge until the middle

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

## Approach: Merge until the middle

> Walk both arrays like a merge, stopping once the middle position is reached.

**Partial merge.** Advance two pointers, always taking the smaller head, until `(m + n) / 2 + 1` values have been taken; keep the last
two taken values to compute the median.

* Time: **O(m + n)** — about half of all values are visited.
* Space: **O(1)** — two pointers and two remembered values.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0004/v1/MedianOfTwoSortedArrays.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0004/v1/MedianOfTwoSortedArraysTest.java` | JUnit 6 tests |
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

* [v2-binary-search-on-the-partition](../v2-binary-search-on-the-partition/README.md): Binary search on the partition (`O(log min(m, n))` time, `O(1)` space)
