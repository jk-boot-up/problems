# 581. Shortest Unsorted Continuous Subarray — v2: Two passes with running max and min

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Array &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/shortest-unsorted-continuous-subarray/)

## Problem

Find the shortest contiguous subarray that, if sorted, makes the whole array sorted ascending. Return its length.

**Example**
```
[2,6,4,8,10,9,15] → 5   (sort [6,4,8,10,9])
[1,2,3,4]         → 0
[1]               → 0
```

**Constraints**
* `1 <= nums.length <= 10^4`

## Approach: Two passes with running max and min

> The right end is the last element smaller than the maximum before it; the left end is the first element bigger than the minimum after it.

**Running extremes.** Left to right, track the maximum so far: any element smaller than it is out of place, so the last such index is the
right end. Right to left, track the minimum so far: the last index (going left) bigger than it is the left end.

* Time: **O(n)** — two passes.
* Space: **O(1)**.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0581/v2/ShortestUnsortedSubarray.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0581/v2/ShortestUnsortedSubarrayTest.java` | JUnit 6 tests |
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

* [v1-compare-with-a-sorted-copy](../v1-compare-with-a-sorted-copy/README.md): Compare with a sorted copy (`O(n log n)` time, `O(n)` space)
