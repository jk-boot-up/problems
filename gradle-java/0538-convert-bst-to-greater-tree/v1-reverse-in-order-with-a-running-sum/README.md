# 538. Convert BST to Greater Tree — v1: Reverse in-order with a running sum

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Binary Search Tree &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/convert-bst-to-greater-tree/)

## Problem

Change every node's value in a BST to the sum of its original value and all values **greater** than it.

**Example**
```
[4,1,6,0,2,5,7,null,null,null,3,null,null,null,8]
  → [30,36,21,36,35,26,15,null,null,null,33,null,null,null,8]
[0,null,1] → [1,null,1]
```

**Constraints**
* `0 <= n <= 10^4`; values are unique

## Approach: Reverse in-order with a running sum

> Visit nodes from largest to smallest (reverse in-order) and keep a running sum.

**Right, root, left.** A reverse in-order walk visits values in decreasing order. Keep `sum` of everything visited; add the current value
to it and store `sum` in the node.

* Time: **O(n)**.
* Space: **O(h)** — recursion depth.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0538/v1/BSTToGreaterTree.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0538/v1/BSTToGreaterTreeTest.java` | JUnit 6 tests |
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
