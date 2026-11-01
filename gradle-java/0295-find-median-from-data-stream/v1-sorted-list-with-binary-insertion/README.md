# 295. Find Median from Data Stream — v1: Sorted list with binary insertion

**Difficulty:** Hard &nbsp;|&nbsp; **Topic:** Heap &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/find-median-from-data-stream/)

## Problem

Implement `MedianFinder`:
* `addNum(int num)`: add a number from the stream;
* `double findMedian()`: the median of all numbers so far (the mean of the two middle values for an even count).

**Example**
```
addNum(1), addNum(2) → findMedian() = 1.5; addNum(3) → findMedian() = 2.0
```

**Constraints**
* `-10^5 <= num <= 10^5`; up to `5 * 10^4` calls; `findMedian` is called on a non-empty stream.

## Approach: Sorted list with binary insertion

> Keep every number in a sorted list; the median is in the middle.

**Insertion sort, one value at a time.** Binary-search the insertion point and insert into an `ArrayList`.

* Time: **O(n)** — per add, because inserting shifts the elements after the position; findMedian is O(1).
* Space: **O(n)** — the list.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0295/v1/MedianFinder.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0295/v1/MedianFinderTest.java` | JUnit 6 tests |
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

* [v2-two-heaps](../v2-two-heaps/README.md): Two heaps (`O(log n)` time, `O(n)` space)
