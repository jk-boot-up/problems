# 154. Find Minimum in Rotated Sorted Array II — v1: Binary search with duplicate shrinking

**Difficulty:** Hard &nbsp;|&nbsp; **Topic:** Binary Search &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/)

## Problem

A sorted array that may contain **duplicates** was rotated. Return its minimum value.

**Example**
```
[1,3,5] → 1,   [2,2,2,0,1] → 0,   [3,1,3] → 1
```

**Constraints**
* `1 <= n <= 5000`

## Approach: Binary search with duplicate shrinking

> Compare mid with hi: bigger → minimum is right, smaller → left half, equal → just drop hi.

**Three cases.** `nums[mid] > nums[hi]`: the minimum is right of mid. `<`: it is mid or left. `==`: we cannot tell, but `nums[hi]` has a copy
at `mid`, so dropping `hi` is safe.

* Time: **O(n)** — worst case with many duplicates; O(log n) for distinct values.
* Space: **O(1)** — indices.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0154/v1/FindMinimumRotatedII.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0154/v1/FindMinimumRotatedIITest.java` | JUnit 6 tests |
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
