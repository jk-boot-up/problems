# 35. Search Insert Position — v1: Lower-bound binary search

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Binary Search &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/search-insert-position/)

## Problem

Given a sorted array of **distinct** integers and a `target`, return the index of `target` if present, otherwise the index where it
would be inserted to keep the order. Run in O(log n).

**Example**
```
nums = [1,3,5,6]:  target 5 → 2,  target 2 → 1,  target 7 → 4
```

**Constraints**
* `1 <= nums.length <= 10^4`; sorted and distinct.

## Approach: Lower-bound binary search

> Binary search for the first index whose value is at least the target.

**Lower bound.** Search `[lo, hi)` with `hi = n`. If `nums[mid] < target`, the answer is right of `mid`; otherwise it is `mid` or
to its left. When `lo == hi`, that is the first index with `nums[i] >= target`.

* Time: **O(log n)** — the range halves each step.
* Space: **O(1)** — two indices.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0035/v1/SearchInsertPosition.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0035/v1/SearchInsertPositionTest.java` | JUnit 6 tests |
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
