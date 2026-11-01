# 162. Find Peak Element — v1: Linear scan

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

## Approach: Linear scan

> Return the first index whose next value is smaller.

**Scan.** The first `i` with `nums[i] > nums[i + 1]` is a peak (everything before it rises). If none, the last index is a peak.

* Time: **O(n)** — a single scan.
* Space: **O(1)** — one index.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0162/v1/FindPeakElement.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0162/v1/FindPeakElementTest.java` | JUnit 6 tests |
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

* [v2-binary-search-uphill](../v2-binary-search-uphill/README.md): Binary search uphill (`O(log n)` time, `O(1)` space)
