# 450. Delete Node in a BST — v1: Recursive delete with successor

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Binary Search Tree &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/delete-node-in-a-bst/)

## Problem

Delete the node with value `key` from a BST (if present) and return the root of the still-valid BST.

**Example**
```
root = [5,3,6,2,4,null,7], key = 3 → [5,4,6,2,null,null,7]  (or [5,2,6,null,4,null,7])
```

**Constraints**
* `0 <= n <= 10^4`; values are unique.

## Approach: Recursive delete with successor

> Find the node; if it has two children, replace its value with its in-order successor and delete that successor instead.

**Three cases.** Recurse toward `key`. A node with no left child is replaced by its right child (and vice versa). A node with two children
copies the smallest value of its right subtree (the in-order successor) and deletes that value from the right subtree.

* Time: **O(h)** — one walk down, plus one walk to the successor.
* Space: **O(h)** — the recursion stack.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0450/v1/DeleteNodeInBST.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0450/v1/DeleteNodeInBSTTest.java` | JUnit 6 tests |
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
