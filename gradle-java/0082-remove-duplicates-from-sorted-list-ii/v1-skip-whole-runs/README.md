# 82. Remove Duplicates from Sorted List II — v1: Skip whole runs

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Linked List &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/)

## Problem

Given the head of a **sorted** linked list, delete every node whose value appears more than once, leaving only values that were
distinct in the original list. Return the sorted result.

**Example 1**
```
Input:  1 → 2 → 3 → 3 → 4 → 4 → 5
Output: 1 → 2 → 5
```

**Example 2**
```
Input:  1 → 1 → 1 → 2 → 3
Output: 2 → 3
```

**Constraints**
* `0 <= n <= 300`; sorted ascending.

## Approach: Skip whole runs

> When a value repeats, skip the whole run; otherwise keep the node.

**Dummy + prev.** `prev` is the last kept node. If `cur` starts a run (`cur.next.val == cur.val`), advance past the whole run and set
`prev.next` to the node after it. Otherwise keep `cur`: `prev = cur`.

* Time: **O(n)** — each node is visited once.
* Space: **O(1)** — pointers only.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0082/v1/RemoveDuplicatesListII.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0082/v1/RemoveDuplicatesListIITest.java` | JUnit 6 tests |
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
