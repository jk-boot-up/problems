# 300. Longest Increasing Subsequence — v1: Quadratic DP

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** 1D DP &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/longest-increasing-subsequence/)

## Problem

Return the length of the longest **strictly increasing subsequence** of `nums` (elements in order, not necessarily contiguous).

**Example**
```
[10,9,2,5,3,7,101,18] → 4   ([2,3,7,101])
[0,1,0,3,2,3]         → 4
[7,7,7,7]             → 1
```

**Constraints**
* `1 <= nums.length <= 2500`

**Follow-up:** O(n log n).

## Approach: Quadratic DP

> len[i] = 1 + the longest len[j] over earlier j with nums[j] < nums[i].

**O(n²) DP.** `len[i]` is the LIS ending at `i`: `1 + max(len[j])` for `j < i` with `nums[j] < nums[i]`.

* Time: **O(n²)** — every pair (j, i) is compared.
* Space: **O(n)** — the len array.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0300/v1/LongestIncreasingSubsequence.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0300/v1/LongestIncreasingSubsequenceTest.java` | JUnit 6 tests |
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

* [v2-tails-array-binary-search](../v2-tails-array-binary-search/README.md): Tails array + binary search (`O(n log n)` time, `O(n)` space)
