# 34. Find First and Last Position of Element in Sorted Array — v1: Two lower bounds

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Binary Search &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/)

## Problem

Given a sorted array `nums`, return the first and last index of `target` as `[first, last]`, or `[-1, -1]` if it is absent. Run in
O(log n).

**Example**
```
nums = [5,7,7,8,8,10]:  target 8 → [3,4],  target 6 → [-1,-1]
```

**Constraints**
* `0 <= nums.length <= 10^5`; sorted non-decreasing.

## Approach: Two lower bounds

> Two lower-bound searches: the first index ≥ target, and the first index ≥ target + 1.

**Lower bound twice.** `lower(x)` is the first index whose value is `>= x`. Then `first = lower(target)`; if it is out of range or not
equal to the target, return `[-1, -1]`. Otherwise `last = lower(target + 1) - 1`.

* Time: **O(log n)** — two binary searches.
* Space: **O(1)** — a few indices.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0034/v1/FirstAndLastPosition.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0034/v1/FirstAndLastPositionTest.java` | JUnit 6 tests |
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
