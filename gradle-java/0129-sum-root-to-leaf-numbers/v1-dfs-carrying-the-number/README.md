# 129. Sum Root to Leaf Numbers — v1: DFS carrying the number

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Binary Tree General &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/sum-root-to-leaf-numbers/)

## Problem

Every node holds a digit `0-9`. Each root-to-leaf path forms a number (e.g. `1 → 2 → 3` is `123`). Return the sum of all
these numbers.

**Example 1**
```
Input:  [1,2,3]
Output: 25   (12 + 13)
```

**Example 2**
```
Input:  [4,9,0,5,1]
Output: 1026   (495 + 491 + 40)
```

**Constraints**
* `1 <= n <= 1000`; depth at most 10; answer fits in 32 bits.

## Approach: DFS carrying the number

> Carry the number formed so far down the tree (times 10 plus the digit) and add it up at the leaves.

**Pass the prefix down.** `dfs(node, prefix)`: `value = prefix * 10 + node.val`. At a leaf return `value`; otherwise return the sum
of both children's results.

* Time: **O(n)** — each node is visited once.
* Space: **O(h)** — the recursion stack.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0129/v1/SumRootToLeaf.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0129/v1/SumRootToLeafTest.java` | JUnit 6 tests |
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
