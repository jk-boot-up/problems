# 101. Symmetric Tree — v1: Iterative queue of pairs

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Binary Tree General &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/symmetric-tree/)

## Problem

Return `true` if a binary tree is a mirror of itself (symmetric around its centre).

**Example 1**
```
Input:  [1,2,2,3,4,4,3]
Output: true
```

**Example 2**
```
Input:  [1,2,2,null,3,null,3]
Output: false
```

**Constraints**
* `1 <= n <= 1000`; `-100 <= Node.val <= 100`

## Approach: Iterative queue of pairs

> Push mirror pairs onto a queue and check them one by one.

**Queue of pairs.** Start with `(root.left, root.right)`. Pop a pair; skip if both null; fail if one is null or the values differ;
otherwise push `(a.left, b.right)` and `(a.right, b.left)`.

* Time: **O(n)** — each node is enqueued once.
* Space: **O(w)** — the queue holds about one level.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0101/v1/SymmetricTree.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0101/v1/SymmetricTreeTest.java` | JUnit 6 tests |
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

* [v2-recursive-mirror-check](../v2-recursive-mirror-check/README.md): Recursive mirror check (`O(n)` time, `O(h)` space)
