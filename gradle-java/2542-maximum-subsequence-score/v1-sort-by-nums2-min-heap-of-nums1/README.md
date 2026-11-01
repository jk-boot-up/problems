# 2542. Maximum Subsequence Score — v1: Sort by nums2 + min-heap of nums1

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Heap &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/maximum-subsequence-score/)

## Problem

Choose `k` indices. The score is `(sum of chosen nums1) × (minimum of chosen nums2)`. Return the maximum score.

**Example**
```
nums1 = [1,3,3,2], nums2 = [2,1,3,4], k = 3 → 12
nums1 = [4,2,3,1,1], nums2 = [7,5,10,9,6], k = 1 → 30
```

**Constraints**
* `1 <= k <= n <= 10^5`

## Approach: Sort by nums2 + min-heap of nums1

> Fix the minimum of nums2 by sorting it in descending order; keep the k largest nums1 values seen so far in a min-heap.

**Enumerate the minimum.** Sort index pairs by `nums2` descending. When we reach pair `i`, its `nums2` is the smallest so far, so it can be
the minimum; pair it with the `k - 1` largest `nums1` values from earlier pairs, maintained in a min-heap with a running sum (in a `long`).

* Time: **O(n log n)** — sorting plus heap operations.
* Space: **O(n)** — the sorted indices and the heap.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p2542/v1/MaximumSubsequenceScore.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p2542/v1/MaximumSubsequenceScoreTest.java` | JUnit 6 tests |
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
