# 704. Binary Search — v1: Classic binary search

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Binary Search &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/binary-search/)

## Problem

Given a sorted array of **distinct** integers and a `target`, return its index or `-1`, in O(log n).

**Example**
```
nums = [-1,0,3,5,9,12]:  target 9 → 4,  target 2 → -1
```

**Constraints**
* `1 <= nums.length <= 10^4`; sorted ascending and distinct.

## Approach: Classic binary search

> Compare with the middle value and discard the half that cannot contain the target.

**Closed interval.** Keep `[lo, hi]`; compare `nums[mid]` with the target and move `lo = mid + 1` or `hi = mid - 1`. Use
`(lo + hi) >>> 1` so the sum cannot overflow.

* Time: **O(log n)** — the range halves each step.
* Space: **O(1)** — three indices.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0704/v1/BinarySearch.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0704/v1/BinarySearchTest.java` | JUnit 6 tests |
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
