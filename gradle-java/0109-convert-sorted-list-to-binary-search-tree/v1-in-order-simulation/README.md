# 109. Convert Sorted List to Binary Search Tree — v1: In-order simulation

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Divide & Conquer &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/)

## Problem

Convert a sorted singly linked list into a height-balanced BST.

**Example**
```
-10 → -3 → 0 → 5 → 9  →  [0,-3,9,-10,null,5]  (one valid answer)
```

**Constraints**
* `0 <= n <= 2 * 10^4`

## Approach: In-order simulation

> Build the tree in in-order: recurse on the left half's size, then consume the list node as the root, then the right half.

**In-order construction.** Count the nodes. `build(lo, hi)` builds the left subtree from `lo..mid-1` first, which advances a shared list
pointer exactly to the middle value; create the root from it, advance, then build the right subtree. No random access is needed.

* Time: **O(n)** — each list node becomes one tree node.
* Space: **O(log n)** — the recursion depth of a balanced tree.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0109/v1/SortedListToBST.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0109/v1/SortedListToBSTTest.java` | JUnit 6 tests |
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
