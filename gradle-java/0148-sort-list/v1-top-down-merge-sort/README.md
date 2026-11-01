# 148. Sort List — v1: Top-down merge sort

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Divide & Conquer &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/sort-list/)

## Problem

Sort a linked list in ascending order and return its head.

**Example**
```
Input:  4 → 2 → 1 → 3
Output: 1 → 2 → 3 → 4
```

**Constraints**
* `0 <= n <= 5 * 10^4`; `-10^5 <= Node.val <= 10^5`

**Follow-up:** O(n log n) time and O(1) memory.

## Approach: Top-down merge sort

> Split at the middle with slow and fast pointers, sort both halves recursively, then merge them.

**Recursive merge sort.** Find the middle with slow/fast pointers, cut the list, sort each half, merge.

* Time: **O(n log n)** — log n levels of linear merging.
* Space: **O(log n)** — the recursion stack.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0148/v1/SortList.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0148/v1/SortListTest.java` | JUnit 6 tests |
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

* [v2-bottom-up-merge-sort-o-1-space](../v2-bottom-up-merge-sort-o-1-space/README.md): Bottom-up merge sort (O(1) space) (`O(n log n)` time, `O(1)` space)
