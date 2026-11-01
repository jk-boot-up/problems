# 100. Same Tree — v1: Recursive comparison

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Binary Tree General &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/same-tree/)

## Problem

Given the roots `p` and `q` of two binary trees, return `true` if they are structurally identical with equal values in every node.

**Example 1**
```
Input:  p = [1,2,3], q = [1,2,3]
Output: true
```

**Example 2**
```
Input:  p = [1,2], q = [1,null,2]
Output: false
```

**Constraints**
* `0 <= n <= 100`; `-10^4 <= Node.val <= 10^4`

## Approach: Recursive comparison

> Two trees are the same when their roots match and both pairs of subtrees are the same.

**Recursion.** Both null → same. One null, or values differ → different. Otherwise compare the left pair and the right pair.

* Time: **O(n)** — each node pair is compared once.
* Space: **O(h)** — the recursion stack.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0100/v1/SameTree.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0100/v1/SameTreeTest.java` | JUnit 6 tests |
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
