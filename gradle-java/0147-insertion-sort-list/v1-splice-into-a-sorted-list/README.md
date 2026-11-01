# 147. Insertion Sort List — v1: Splice into a sorted list

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Linked List &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/insertion-sort-list/)

## Problem

Sort a linked list using insertion sort and return its head.

**Example**
```
4 → 2 → 1 → 3 becomes 1 → 2 → 3 → 4,   -1 → 5 → 3 → 4 → 0 becomes -1 → 0 → 3 → 4 → 5
```

**Constraints**
* `1 <= n <= 5000`

## Approach: Splice into a sorted list

> Take nodes one by one and splice each into its place in a growing sorted list.

**Dummy-headed sorted list.** For each node, walk from the dummy to find the last node smaller than it and splice it in. (A small speed-up:
restart the walk only when the new value is smaller than the previous insertion point.)

* Time: **O(n²)** — each insertion may walk the whole sorted part.
* Space: **O(1)** — nodes are re-linked.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0147/v1/InsertionSortList.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0147/v1/InsertionSortListTest.java` | JUnit 6 tests |
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
