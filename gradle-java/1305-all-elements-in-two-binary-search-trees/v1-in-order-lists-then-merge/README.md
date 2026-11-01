# 1305. All Elements in Two Binary Search Trees — v1: In-order lists, then merge

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Binary Search Tree &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/all-elements-in-two-binary-search-trees/)

## Problem

Return all values from two BSTs in one ascending list.

**Example**
```
root1 = [2,1,4], root2 = [1,0,3]   → [0,1,1,2,3,4]
root1 = [1,null,8], root2 = [8,1]  → [1,1,8,8]
```

**Constraints**
* `0 <= nodes per tree <= 5000`

## Approach: In-order lists, then merge

> An in-order walk of each tree is sorted; merge the two sorted lists.

**Two sorted runs.** An in-order traversal of a BST yields its values in order. Collect both (iteratively, with a stack) and merge them
like in merge sort.

* Time: **O(m + n)**.
* Space: **O(m + n)** — the lists.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p1305/v1/AllElementsTwoBST.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p1305/v1/AllElementsTwoBSTTest.java` | JUnit 6 tests |
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
