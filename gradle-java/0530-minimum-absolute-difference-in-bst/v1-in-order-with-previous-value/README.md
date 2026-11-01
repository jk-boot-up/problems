# 530. Minimum Absolute Difference in BST — v1: In-order with previous value

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Binary Search Tree &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/minimum-absolute-difference-in-bst/)

## Problem

Given the root of a **BST**, return the minimum absolute difference between the values of any two different nodes.

**Example 1**
```
Input:  [4,2,6,1,3]
Output: 1
```

**Example 2**
```
Input:  [1,0,48,null,null,12,49]
Output: 1
```

**Constraints**
* `2 <= n <= 10^4`; `0 <= Node.val <= 10^5`

## Approach: In-order with previous value

> In-order traversal of a BST is sorted, so the closest pair is always adjacent in that order.

**Sorted order.** An in-order traversal visits values in increasing order; compare each value with the previous one and keep the smallest gap.

* Time: **O(n)** — one traversal.
* Space: **O(h)** — the recursion stack.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0530/v1/MinimumDifferenceBST.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0530/v1/MinimumDifferenceBSTTest.java` | JUnit 6 tests |
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
