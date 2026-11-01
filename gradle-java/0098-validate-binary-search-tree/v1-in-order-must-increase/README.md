# 98. Validate Binary Search Tree — v1: In-order must increase

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Binary Search Tree &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/validate-binary-search-tree/)

## Problem

Return `true` if a binary tree is a valid **BST**: every node's left subtree holds only smaller values, its right subtree only larger
values, and both subtrees are BSTs.

**Example 1**
```
Input:  [2,1,3]
Output: true
```

**Example 2**
```
Input:  [5,1,4,null,null,3,6]
Output: false   (3 is in the right subtree of 5 but smaller than 5)
```

**Constraints**
* `1 <= n <= 10^4`; `-2^31 <= Node.val <= 2^31 - 1`

## Approach: In-order must increase

> A BST's in-order traversal is strictly increasing; check each value against the previous one.

**Sorted check.** Traverse in order, keeping the previous value; any value not greater than it means the tree is not a BST.

* Time: **O(n)** — one traversal.
* Space: **O(h)** — the recursion stack.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0098/v1/ValidateBST.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0098/v1/ValidateBSTTest.java` | JUnit 6 tests |
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

* [v2-bounds-recursion](../v2-bounds-recursion/README.md): Bounds recursion (`O(n)` time, `O(h)` space)
