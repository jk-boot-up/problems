# 23. Merge k Sorted Lists — v1: Min-heap of list heads

**Difficulty:** Hard &nbsp;|&nbsp; **Topic:** Divide & Conquer &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/merge-k-sorted-lists/)

## Problem

You are given an array of `k` linked lists, each sorted ascending. Merge them into one sorted linked list and return its head.

**Example**
```
Input:  [[1,4,5],[1,3,4],[2,6]]
Output: 1 → 1 → 2 → 3 → 4 → 4 → 5 → 6
```

**Constraints**
* `0 <= k <= 10^4`; total nodes `N <= 10^4`

## Approach: Min-heap of list heads

> A priority queue always hands out the smallest current head among the k lists.

**Priority queue.** Push every non-null head into a min-heap keyed by value. Pop the smallest, append it, and push its `next`.

* Time: **O(N log k)** — each of N nodes is pushed and popped from a heap of size k.
* Space: **O(k)** — the heap.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0023/v1/MergeKSortedLists.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0023/v1/MergeKSortedListsTest.java` | JUnit 6 tests |
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

* [v2-pairwise-divide-and-conquer](../v2-pairwise-divide-and-conquer/README.md): Pairwise divide and conquer (`O(N log k)` time, `O(1)` space)
