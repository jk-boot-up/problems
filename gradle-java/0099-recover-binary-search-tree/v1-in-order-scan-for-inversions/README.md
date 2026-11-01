# 99. Recover Binary Search Tree — v1: In-order scan for inversions

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Binary Search Tree &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/recover-binary-search-tree/)

## Problem

Exactly two nodes of a BST had their values swapped by mistake. Recover the tree **without changing its structure**.

**Example**
```
[1,3,null,null,2] → [3,1,null,null,2]
[3,1,4,null,null,2] → [2,1,4,null,null,3]
```

**Constraints**
* `2 <= n <= 1000`

## Approach: In-order scan for inversions

> In-order order of a BST is sorted; the two swapped nodes show up as the first and last 'descents'.

**Find the inversions.** During an in-order traversal, a node smaller than its predecessor is a descent. The first swapped node is the
predecessor of the first descent; the second is the current node of the last descent (adjacent swaps give a single descent). Swap their
values back.

* Time: **O(n)** — one traversal.
* Space: **O(h)** — the traversal stack.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0099/v1/RecoverBST.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0099/v1/RecoverBSTTest.java` | JUnit 6 tests |
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
