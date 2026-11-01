# 912. Sort an Array — v2: Merge sort

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Sorting &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/sort-an-array/)

## Problem

Sort `nums` in ascending order **without** built-in sort functions, in O(n log n) time and with as little extra space as possible.

**Example**
```
[5,2,3,1] → [1,2,3,5],   [5,1,1,2,0,0] → [0,0,1,1,2,5]
```

**Constraints**
* `1 <= nums.length <= 5 * 10^4`

## Approach: Merge sort

> Merge sort: split in half, sort both halves, merge them; always O(n log n).

**Top-down merge sort** with one shared buffer: sort `[lo, mid]` and `[mid+1, hi]`, then merge them through the buffer.

* Time: **O(n log n)** — log n levels of linear merges.
* Space: **O(n)** — the buffer.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0912/v2/SortAnArray.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0912/v2/SortAnArrayTest.java` | JUnit 6 tests |
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

* [v1-heap-sort-in-place](../v1-heap-sort-in-place/README.md): Heap sort (in place) (`O(n log n)` time, `O(1)` space)
