# 162. Find Peak Element — v2: Binary search uphill

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Binary Search &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/find-peak-element/)

## Problem

A **peak** is an element strictly greater than its neighbours. Given `nums` (with `nums[-1] = nums[n] = -∞` and no two adjacent values
equal), return the index of **any** peak, in O(log n).

**Example**
```
Input:  nums = [1,2,1,3,5,6,4]
Output: 1 or 5
```

**Constraints**
* `1 <= nums.length <= 1000`; `nums[i] != nums[i + 1]`

## Approach: Binary search uphill

> Walk uphill: if the next element is larger, a peak lies to the right; otherwise mid is on a downslope or a peak.

**Follow the slope.** If `nums[mid] < nums[mid + 1]`, the values rise to the right and must eventually come down (the edge is −∞),
so a peak exists in `mid + 1 .. hi`. Otherwise a peak exists in `lo .. mid`. Stop when `lo == hi`.

* Time: **O(log n)** — the range halves each step.
* Space: **O(1)** — two indices.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0162/v2/FindPeakElement.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0162/v2/FindPeakElementTest.java` | JUnit 6 tests |
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

* [v1-linear-scan](../v1-linear-scan/README.md): Linear scan (`O(n)` time, `O(1)` space)
