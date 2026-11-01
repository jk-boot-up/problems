# 1493. Longest Subarray of 1's After Deleting One Element — v1: Sliding window with one zero

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Sliding Window &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/)

## Problem

Delete exactly one element from a binary array. Return the length of the longest non-empty subarray of only `1`s in the result (0 if none).

**Example**
```
[1,1,0,1] → 3,   [0,1,1,1,0,1,1,0,1] → 5,   [1,1,1] → 2
```

**Constraints**
* `1 <= nums.length <= 10^5`

## Approach: Sliding window with one zero

> A window with at most one zero; its length minus one (the deleted element) is a candidate.

**At most one zero.** Same as Max Consecutive Ones III with `k = 1`, but one element must be deleted, so the answer is the window length
minus 1 (this also covers an all-ones array).

* Time: **O(n)** — one pass.
* Space: **O(1)** — a counter.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p1493/v1/LongestSubarrayAfterDeleting.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p1493/v1/LongestSubarrayAfterDeletingTest.java` | JUnit 6 tests |
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
