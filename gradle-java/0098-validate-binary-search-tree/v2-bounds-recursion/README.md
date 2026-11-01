# 98. Validate Binary Search Tree — v2: Bounds recursion

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

## Approach: Bounds recursion

> Every node must lie strictly inside the (low, high) window inherited from its ancestors.

**Pass down bounds.** `valid(n, low, high)` requires `low < n.val < high`; the left child gets `(low, n.val)` and the right child
`(n.val, high)`. Use `long` bounds so values equal to `Integer.MIN_VALUE` / `MAX_VALUE` work.

* Time: **O(n)** — each node is checked once.
* Space: **O(h)** — the recursion stack.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0098/v2/ValidateBST.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0098/v2/ValidateBSTTest.java` | JUnit 6 tests |
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

* [v1-in-order-must-increase](../v1-in-order-must-increase/README.md): In-order must increase (`O(n)` time, `O(h)` space)
