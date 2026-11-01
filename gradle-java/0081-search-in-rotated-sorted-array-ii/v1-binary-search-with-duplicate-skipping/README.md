# 81. Search in Rotated Sorted Array II — v1: Binary search with duplicate skipping

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Binary Search &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/search-in-rotated-sorted-array-ii/)

## Problem

A sorted array, possibly with **duplicates**, was rotated. Return `true` if `target` is in it.

**Example**
```
nums = [2,5,6,0,0,1,2]: target 0 → true, target 3 → false
```

**Constraints**
* `1 <= nums.length <= 5000`

**Follow-up:** duplicates can make the worst case linear — why?

## Approach: Binary search with duplicate skipping

> Like the distinct version, but when lo, mid and hi are equal the sorted half is unknown, so shrink both ends.

**Pick the sorted half when possible.** If `nums[lo] == nums[mid] == nums[hi]`, either half could hold the rotation, so just move `lo++`,
`hi--`. Otherwise one half is sorted; check whether the target lies inside it, exactly as in the distinct version.

* Time: **O(n)** — worst case with many duplicates; O(log n) when values are distinct.
* Space: **O(1)** — indices.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0081/v1/SearchRotatedArrayII.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0081/v1/SearchRotatedArrayIITest.java` | JUnit 6 tests |
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
