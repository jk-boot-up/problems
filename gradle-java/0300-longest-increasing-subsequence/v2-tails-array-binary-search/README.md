# 300. Longest Increasing Subsequence — v2: Tails array + binary search

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

## Approach: Tails array + binary search

> Patience sorting: tails[k] is the smallest possible tail of an increasing subsequence of length k + 1.

**Smallest tails.** Keep `tails` sorted: `tails[k]` is the smallest tail value of any increasing subsequence of length `k + 1`. For each
`x`, binary-search the first tail `>= x` and replace it with `x` (or append `x` if all tails are smaller). The length of `tails` is the
answer (its contents are not necessarily a real subsequence).

* Time: **O(n log n)** — one binary search per element.
* Space: **O(n)** — the tails array.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0300/v2/LongestIncreasingSubsequence.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0300/v2/LongestIncreasingSubsequenceTest.java` | JUnit 6 tests |
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

* [v1-quadratic-dp](../v1-quadratic-dp/README.md): Quadratic DP (`O(n²)` time, `O(n)` space)
