# 872. Leaf-Similar Trees — v1: Collect leaf sequences

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Binary Tree General &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/leaf-similar-trees/)

## Problem

Two binary trees are **leaf-similar** if their leaf values, read left to right, form the same sequence. Return whether `root1` and `root2`
are leaf-similar.

**Example**
```
[3,5,1,6,2,9,8,null,null,7,4] and [3,5,1,6,7,4,2,null,null,null,null,null,null,9,8] → true
[1,2,3] and [1,3,2] → false
```

**Constraints**
* `1 <= nodes <= 200`

## Approach: Collect leaf sequences

> Collect each tree's leaves left to right and compare the two sequences.

**DFS to the leaves.** A left-first DFS lists leaves in left-to-right order; compare the two lists.

* Time: **O(n + m)** — both trees once.
* Space: **O(n + m)** — the leaf lists and recursion.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0872/v1/LeafSimilarTrees.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0872/v1/LeafSimilarTreesTest.java` | JUnit 6 tests |
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
