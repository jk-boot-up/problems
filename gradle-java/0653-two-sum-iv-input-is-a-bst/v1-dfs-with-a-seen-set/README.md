# 653. Two Sum IV - Input is a BST — v1: DFS with a seen set

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Binary Search Tree &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/two-sum-iv-input-is-a-bst/)

## Problem

Return `true` if two different nodes of the BST have values summing to `k`.

**Example**
```
root = [5,3,6,2,4,null,7], k = 9 → true,   k = 28 → false
```

**Constraints**
* `1 <= n <= 10^4`

## Approach: DFS with a seen set

> Traverse the tree, checking whether k − value has already been seen.

**Hash set.** Visit every node; if `k - val` is in the `MyHashSet`, return true; otherwise add `val`.

* Time: **O(n)** — each node once.
* Space: **O(n)** — the set.

Hash lookups use `MyHashMap` / `MyHashSet`, our own hash table (bucket array, chaining, resizing), instead of `java.util.HashMap`.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0653/v1/TwoSumIV.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0653/v1/TwoSumIVTest.java` | JUnit 6 tests |
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
