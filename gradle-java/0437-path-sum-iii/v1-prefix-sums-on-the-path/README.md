# 437. Path Sum III — v1: Prefix sums on the path

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Binary Tree General &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/path-sum-iii/)

## Problem

Count the downward paths (from a node to one of its descendants, not necessarily root or leaf) whose values sum to `targetSum`.

**Example**
```
root = [10,5,-3,3,2,null,11,3,-2,null,1], targetSum = 8 → 3
```

**Constraints**
* `0 <= n <= 1000`; sums may need 64 bits.

## Approach: Prefix sums on the path

> Prefix sums along the root-to-node path: a downward path ending here sums to target when an earlier prefix equals current − target.

**Prefix-sum counts.** Keep a `MyHashMap` of prefix sums on the current root-to-node path. At each node, add the count of
`prefix - target`, insert the new prefix, recurse, then remove it when backtracking.

* Time: **O(n)** — O(1) map work per node.
* Space: **O(h)** — the map holds one entry per path node, plus the recursion.

Hash lookups use `MyHashMap` / `MyHashSet`, our own hash table (bucket array, chaining, resizing), instead of `java.util.HashMap`.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0437/v1/PathSumIII.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0437/v1/PathSumIIITest.java` | JUnit 6 tests |
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
