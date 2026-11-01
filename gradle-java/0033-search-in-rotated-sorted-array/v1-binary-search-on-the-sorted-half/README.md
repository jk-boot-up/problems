# 33. Search in Rotated Sorted Array — v1: Binary search on the sorted half

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Binary Search &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/search-in-rotated-sorted-array/)

## Problem

A sorted array of **distinct** integers was rotated at an unknown pivot (e.g. `[0,1,2,4,5,6,7]` → `[4,5,6,7,0,1,2]`). Return the index
of `target`, or `-1`, in O(log n).

**Example**
```
nums = [4,5,6,7,0,1,2]:  target 0 → 4,  target 3 → -1
```

**Constraints**
* `1 <= nums.length <= 5000`; values are distinct.

## Approach: Binary search on the sorted half

> One half around mid is always sorted; check whether the target lies inside that sorted half.

**Pick the sorted half.** If `nums[lo] <= nums[mid]`, the left half `lo..mid` is sorted: go left if the target lies in
`[nums[lo], nums[mid])`, otherwise go right. Otherwise the right half `mid..hi` is sorted: go right if the target lies in
`(nums[mid], nums[hi]]`, otherwise go left.

* Time: **O(log n)** — the range halves each step.
* Space: **O(1)** — a few indices.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0033/v1/SearchRotatedArray.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0033/v1/SearchRotatedArrayTest.java` | JUnit 6 tests |
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
