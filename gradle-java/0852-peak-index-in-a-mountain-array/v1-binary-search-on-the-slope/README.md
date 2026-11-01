# 852. Peak Index in a Mountain Array — v1: Binary search on the slope

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Binary Search &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/peak-index-in-a-mountain-array/)

## Problem

`arr` strictly increases then strictly decreases. Return the index of the peak in O(log n).

**Example**
```
[0,1,0] → 1,   [0,2,1,0] → 1,   [0,10,5,2] → 1
```

**Constraints**
* `3 <= arr.length <= 10^5`

## Approach: Binary search on the slope

> Binary search on the slope: if arr[mid] < arr[mid + 1] the peak is to the right, otherwise at mid or to the left.

**Follow the slope.** Same as Find Peak Element: move right while rising, otherwise move `hi` to `mid`.

* Time: **O(log n)** — binary search.
* Space: **O(1)** — two indices.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0852/v1/PeakIndexInMountain.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0852/v1/PeakIndexInMountainTest.java` | JUnit 6 tests |
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
