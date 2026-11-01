# 173. Binary Search Tree Iterator — v2: Controlled stack

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Binary Tree General &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/binary-search-tree-iterator/)

## Problem

Implement an iterator over a BST that returns values in **ascending** (in-order) order:
* `BSTIterator(TreeNode root)`
* `int next()`: the next smallest value (always valid when called)
* `boolean hasNext()`

**Example**
```
root = [7,3,15,null,null,9,20]
next() → 3, next() → 7, hasNext() → true, next() → 9, next() → 15, next() → 20, hasNext() → false
```

**Constraints**
* `1 <= n <= 10^5`

**Follow-up:** O(1) average time per call and O(h) memory.

## Approach: Controlled stack

> Keep a stack of the leftmost path; next() pops a node and pushes the leftmost path of its right child.

**Stack of pending ancestors.** Push the whole left spine from the root. `next()` pops the top (the smallest unvisited value), then
pushes the left spine of its right child.

* Time: **O(1)** — amortized per call: each node is pushed and popped once over the whole iteration.
* Space: **O(h)** — the stack holds at most one root-to-leaf path.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0173/v2/BSTIterator.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0173/v2/BSTIteratorTest.java` | JUnit 6 tests |
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

* [v1-flatten-to-a-list-first](../v1-flatten-to-a-list-first/README.md): Flatten to a list first (`O(1)` time, `O(n)` space)
