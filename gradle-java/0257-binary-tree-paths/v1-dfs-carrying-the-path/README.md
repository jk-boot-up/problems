# 257. Binary Tree Paths — v1: DFS carrying the path

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Binary Tree DFS &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/binary-tree-paths/)

## Problem

Return all root-to-leaf paths of a binary tree, in any order, written as `"a->b->c"`.

**Example**
```
[1,2,3,null,5] → ["1->2->5","1->3"]
[1]            → ["1"]
```

**Constraints**
* `1 <= n <= 100`

## Approach: DFS carrying the path

> Carry the path string down; at a leaf, the path is complete.

**DFS.** Pass the path so far into each call. Append the current value; at a leaf, record the path; otherwise recurse into the children
with `"->"` appended. A `StringBuilder` that is trimmed back after each call avoids copying.

* Time: **O(n · h)** — each leaf's path has up to `h` values to write.
* Space: **O(h)** — the recursion and the builder.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0257/v1/BinaryTreePaths.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0257/v1/BinaryTreePathsTest.java` | JUnit 6 tests |
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
