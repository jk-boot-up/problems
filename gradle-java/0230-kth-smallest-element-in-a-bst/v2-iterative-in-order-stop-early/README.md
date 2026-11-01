# 230. Kth Smallest Element in a BST — v2: Iterative in-order, stop early

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Binary Search Tree &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/kth-smallest-element-in-a-bst/)

## Problem

Given the root of a BST and an integer `k`, return the `k`-th smallest value (1-indexed).

**Example 1**
```
Input:  root = [3,1,4,null,2], k = 1
Output: 1
```

**Example 2**
```
Input:  root = [5,3,6,2,4,null,null,1], k = 3
Output: 3
```

**Constraints**
* `1 <= k <= n <= 10^4`

## Approach: Iterative in-order, stop early

> Walk the BST in order and stop at the k-th visited node.

**Stack-based in-order.** Push the left spine; pop a node (the next smallest), decrement `k`; when `k` hits 0, return it. Otherwise
push the left spine of its right child.

* Time: **O(h + k)** — descend once, then pop k nodes.
* Space: **O(h)** — the stack.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0230/v2/KthSmallestBST.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0230/v2/KthSmallestBSTTest.java` | JUnit 6 tests |
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

* [v1-full-in-order-list](../v1-full-in-order-list/README.md): Full in-order list (`O(n)` time, `O(n)` space)
