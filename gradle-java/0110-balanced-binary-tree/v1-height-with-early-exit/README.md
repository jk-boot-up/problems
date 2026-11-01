# 110. Balanced Binary Tree — v1: Height with early exit

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Binary Tree General &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/balanced-binary-tree/)

## Problem

Return `true` if a binary tree is **height-balanced**: for every node, the heights of its two subtrees differ by at most 1.

**Example**
```
[3,9,20,null,null,15,7]     → true
[1,2,2,3,3,null,null,4,4]   → false
```

**Constraints**
* `0 <= n <= 5000`

## Approach: Height with early exit

> Compute heights bottom-up and return −1 as soon as any node's subtrees differ by more than one.

**Post-order heights.** `height(n)` returns -1 if the subtree is unbalanced, otherwise its height. Each node checks both child heights
once, so the whole tree is checked in one pass.

* Time: **O(n)** — each node once.
* Space: **O(h)** — the recursion stack.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0110/v1/BalancedBinaryTree.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0110/v1/BalancedBinaryTreeTest.java` | JUnit 6 tests |
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
