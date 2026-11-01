# 108. Convert Sorted Array to Binary Search Tree — v1: Middle element as root

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Divide & Conquer &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/)

## Problem

Given a strictly increasing array `nums`, build a **height-balanced** BST (the depths of the two subtrees of every node differ by at
most one). Any valid answer is accepted.

**Example**
```
Input:  nums = [-10,-3,0,5,9]
Output: [0,-3,9,-10,null,5]   (one possible answer)
```

**Constraints**
* `1 <= nums.length <= 10^4`; strictly increasing.

## Approach: Middle element as root

> The middle element becomes the root; the left and right halves become balanced subtrees.

**Divide and conquer.** `build(lo, hi)`: the middle index `mid = (lo + hi) / 2` is the root; build the left subtree from `lo..mid-1`
and the right from `mid+1..hi`. Halving keeps the tree balanced.

* Time: **O(n)** — each element becomes exactly one node.
* Space: **O(log n)** — the recursion depth.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0108/v1/SortedArrayToBST.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0108/v1/SortedArrayToBSTTest.java` | JUnit 6 tests |
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
