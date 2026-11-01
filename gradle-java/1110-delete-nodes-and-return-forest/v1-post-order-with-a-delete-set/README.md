# 1110. Delete Nodes And Return Forest — v1: Post-order with a delete set

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Binary Tree DFS &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/delete-nodes-and-return-forest/)

## Problem

Delete every node whose value is in `to_delete`. The remaining nodes form a forest; return the roots of its trees, in any order.

**Example**
```
root = [1,2,3,4,5,6,7], to_delete = [3,5] → [[1,2,null,4],[6],[7]]
root = [1,2,4,null,3],  to_delete = [3]   → [[1,2,4]]
```

**Constraints**
* `1 <= n <= 1000`, distinct values

## Approach: Post-order with a delete set

> Post-order: when a node is deleted, its surviving children become new roots.

**Children first.** Put `to_delete` in a `MyHashSet`. Recurse with a flag saying whether the node's parent was deleted (or it is the root).
A kept node with that flag set is a new root. Process children before deciding, and return `null` for a deleted node so its parent
unlinks it.

* Time: **O(n + d)**.
* Space: **O(h + d)** — recursion and the set.

Hash lookups use `MyHashMap` / `MyHashSet`, our own hash table (bucket array, chaining, resizing), instead of `java.util.HashMap`.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p1110/v1/DeleteNodesForest.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p1110/v1/DeleteNodesForestTest.java` | JUnit 6 tests |
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
