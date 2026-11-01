# 21. Merge Two Sorted Lists — v1: Recursive

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Linked List &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/merge-two-sorted-lists/)

## Problem

Merge two sorted linked lists `list1` and `list2` into one sorted list by splicing their nodes together. Return its head.

**Example 1**
```
Input:  list1 = 1 → 2 → 4, list2 = 1 → 3 → 4
Output: 1 → 1 → 2 → 3 → 4 → 4
```

**Example 2**
```
Input:  list1 = null, list2 = 0
Output: 0
```

**Constraints**
* `0..50` nodes per list; `-100 <= Node.val <= 100`; both sorted non-decreasing.

## Approach: Recursive

> The smaller head comes first; its next is the merge of everything that remains.

**Recursion.** If either list is empty, return the other. Otherwise the smaller head wins and its `next` becomes
`mergeTwoLists(winner.next, other)`.

* Time: **O(m + n)** — one call per node.
* Space: **O(m + n)** — the recursion depth.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0021/v1/MergeTwoSortedLists.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0021/v1/MergeTwoSortedListsTest.java` | JUnit 6 tests |
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

* [v2-iterative-with-dummy-head](../v2-iterative-with-dummy-head/README.md): Iterative with dummy head (`O(m + n)` time, `O(1)` space)
