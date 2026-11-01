# 373. Find K Pairs with Smallest Sums — v1: Min-heap over row heads

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Heap &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/find-k-pairs-with-smallest-sums/)

## Problem

Given two sorted arrays `nums1` and `nums2` and an integer `k`, return the `k` pairs `[u, v]` (u from nums1, v from nums2) with the
smallest sums.

**Example**
```
Input:  nums1 = [1,7,11], nums2 = [2,4,6], k = 3
Output: [[1,2],[1,4],[1,6]]
```

**Constraints**
* `1 <= nums1.length, nums2.length <= 10^5`; `1 <= k <= 10^4`; `k <= nums1.length * nums2.length`

## Approach: Min-heap over row heads

> Treat each nums1[i] as a sorted row of pairs; a heap merges the rows, always expanding the smallest pair.

**K-way merge.** Row `i` is the pairs `(nums1[i], nums2[0..])`, already sorted by sum. Seed a min-heap with `(i, 0)` for the first
`min(k, n1)` rows. Pop the smallest, record it, and push `(i, j + 1)` from the same row.

* Time: **O(k log k)** — k pops and pushes on a heap of size at most k.
* Space: **O(k)** — the heap (plus the output).

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0373/v1/KSmallestPairs.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0373/v1/KSmallestPairsTest.java` | JUnit 6 tests |
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
* **Complexity:** time and space cost, plotted against the common growth curves.

Switch between Light, Medium and Dark themes in the header.
