# 23. Merge k Sorted Lists — v2: Pairwise divide and conquer

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

## Approach: Pairwise divide and conquer

> Merge the lists in pairs, round after round, like the upper levels of merge sort.

**Merge in rounds.** In each round merge list `i` with list `i + step` for `step = 1, 2, 4, …`. Each round halves the number of lists,
and every node takes part in one merge per round.

* Time: **O(N log k)** — log k rounds, each touching all N nodes.
* Space: **O(1)** — nodes are re-linked in place.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0023/v2/MergeKSortedLists.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0023/v2/MergeKSortedListsTest.java` | JUnit 6 tests |
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

* [v1-min-heap-of-list-heads](../v1-min-heap-of-list-heads/README.md): Min-heap of list heads (`O(N log k)` time, `O(k)` space)
