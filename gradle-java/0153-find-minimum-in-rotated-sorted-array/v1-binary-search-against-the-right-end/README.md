# 153. Find Minimum in Rotated Sorted Array — v1: Binary search against the right end

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Binary Search &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/)

## Problem

A sorted array of **unique** values was rotated between 1 and n times. Return its minimum element in O(log n).

**Example**
```
[3,4,5,1,2] → 1,  [4,5,6,7,0,1,2] → 0,  [11,13,15,17] → 11
```

**Constraints**
* `1 <= n <= 5000`; values are unique.

## Approach: Binary search against the right end

> Compare mid with the right end: if mid is bigger, the drop (and the minimum) is to its right.

**Look for the drop.** If `nums[mid] > nums[hi]`, the rotation point is right of `mid`: `lo = mid + 1`. Otherwise `mid..hi` is sorted,
so the minimum is at `mid` or to its left: `hi = mid`.

* Time: **O(log n)** — the range halves each step.
* Space: **O(1)** — two indices.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0153/v1/FindMinimumRotated.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0153/v1/FindMinimumRotatedTest.java` | JUnit 6 tests |
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
