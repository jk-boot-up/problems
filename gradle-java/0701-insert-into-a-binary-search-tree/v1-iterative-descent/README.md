# 701. Insert into a Binary Search Tree — v1: Iterative descent

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Binary Search Tree &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/insert-into-a-binary-search-tree/)

## Problem

Insert `val` (not already present) into a BST and return the root. Any valid BST is accepted.

**Example**
```
root = [4,2,7,1,3], val = 5 → [4,2,7,1,3,5]
```

**Constraints**
* `0 <= n <= 10^4`

## Approach: Iterative descent

> Walk down as if searching for the value; attach it where the search falls off the tree.

**Search, then attach.** Descend left or right; when the chosen child is null, place the new node there.

* Time: **O(h)** — one root-to-leaf path.
* Space: **O(1)** — iterative.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0701/v1/InsertIntoBST.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0701/v1/InsertIntoBSTTest.java` | JUnit 6 tests |
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
