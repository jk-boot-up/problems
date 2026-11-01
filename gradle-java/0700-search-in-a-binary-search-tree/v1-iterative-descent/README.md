# 700. Search in a Binary Search Tree — v1: Iterative descent

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Binary Search Tree &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/search-in-a-binary-search-tree/)

## Problem

Return the subtree rooted at the node whose value is `val` in a BST, or `null` if it does not exist.

**Example**
```
root = [4,2,7,1,3], val = 2 → [2,1,3],   val = 5 → null
```

**Constraints**
* `1 <= n <= 5000`

## Approach: Iterative descent

> Compare with the current node and go left or right; the BST order tells you which way.

**Descend.** While the node exists and differs from `val`, move to `left` if `val` is smaller, else `right`.

* Time: **O(h)** — one root-to-node path.
* Space: **O(1)** — iterative.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0700/v1/SearchInBST.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0700/v1/SearchInBSTTest.java` | JUnit 6 tests |
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
