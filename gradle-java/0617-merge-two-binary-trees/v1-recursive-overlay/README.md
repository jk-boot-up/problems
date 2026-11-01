# 617. Merge Two Binary Trees — v1: Recursive overlay

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Binary Tree General &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/merge-two-binary-trees/)

## Problem

Merge two binary trees: overlapping nodes sum their values; a node present in only one tree is used as is. Return the merged tree.

**Example**
```
root1 = [1,3,2,5], root2 = [2,1,3,null,4,null,7] → [3,4,5,5,4,null,7]
```

**Constraints**
* `0 <= nodes <= 2000`

## Approach: Recursive overlay

> Overlay the trees: where both have a node, add the values; otherwise take whichever node exists.

**Recursion.** If either side is null return the other; otherwise add the values into `t1` and merge the children pairwise.

* Time: **O(min(n, m))** — only overlapping nodes are visited.
* Space: **O(h)** — the recursion stack.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0617/v1/MergeTwoBinaryTrees.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0617/v1/MergeTwoBinaryTreesTest.java` | JUnit 6 tests |
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
