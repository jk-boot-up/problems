# 230. Kth Smallest Element in a BST — v1: Full in-order list

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

## Approach: Full in-order list

> Collect every value in sorted order, then index k − 1.

**Collect everything.** A recursive in-order traversal fills a list; return `list.get(k - 1)`.

* Time: **O(n)** — the whole tree is traversed even for small k.
* Space: **O(n)** — the list.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0230/v1/KthSmallestBST.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0230/v1/KthSmallestBSTTest.java` | JUnit 6 tests |
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

* [v2-iterative-in-order-stop-early](../v2-iterative-in-order-stop-early/README.md): Iterative in-order, stop early (`O(h + k)` time, `O(h)` space)
