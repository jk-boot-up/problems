# 912. Sort an Array — v1: Heap sort (in place)

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Sorting &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/sort-an-array/)

## Problem

Sort `nums` in ascending order **without** built-in sort functions, in O(n log n) time and with as little extra space as possible.

**Example**
```
[5,2,3,1] → [1,2,3,5],   [5,1,1,2,0,0] → [0,0,1,1,2,5]
```

**Constraints**
* `1 <= nums.length <= 5 * 10^4`

## Approach: Heap sort (in place)

> Build a max-heap in the array, then repeatedly swap the maximum to the end and repair the heap.

**Heap sort.** Heapify bottom-up; then for `end = n-1 .. 1`, swap `a[0]` with `a[end]` and sift the new root down within `[0, end)`.

* Time: **O(n log n)** — n sift-downs of O(log n).
* Space: **O(1)** — in place.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0912/v1/SortAnArray.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0912/v1/SortAnArrayTest.java` | JUnit 6 tests |
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

* [v2-merge-sort](../v2-merge-sort/README.md): Merge sort (`O(n log n)` time, `O(n)` space)
