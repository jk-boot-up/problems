# 31. Next Permutation — v1: Pivot, swap, reverse

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Two Pointers &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/next-permutation/)

## Problem

Rearrange `nums` **in place** into the next lexicographically greater permutation. If it is the largest permutation, rearrange it
into the smallest (ascending) one.

**Example**
```
[1,2,3] → [1,3,2],   [3,2,1] → [1,2,3],   [1,1,5] → [1,5,1]
```

**Constraints**
* `1 <= nums.length <= 100`

## Approach: Pivot, swap, reverse

> Find the rightmost ascent, swap its left value with the next larger value to its right, then reverse the tail.

**Three steps.** (1) From the right, find the first `i` with `nums[i] < nums[i+1]` (the pivot); the tail after it is non-increasing.
(2) If found, swap `nums[i]` with the rightmost value in the tail that is larger than it. (3) Reverse the tail, making it ascending.

* Time: **O(n)** — at most three linear scans.
* Space: **O(1)** — in place.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0031/v1/NextPermutation.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0031/v1/NextPermutationTest.java` | JUnit 6 tests |
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
