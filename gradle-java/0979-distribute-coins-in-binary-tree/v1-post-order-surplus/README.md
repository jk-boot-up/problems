# 979. Distribute Coins in Binary Tree — v1: Post-order surplus

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Binary Tree DFS &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/distribute-coins-in-binary-tree/)

## Problem

A binary tree has `n` nodes and `n` coins in total (`node.val` coins on each node). One move sends one coin across one edge. Return the
fewest moves so that every node has exactly one coin.

**Example**
```
[3,0,0] → 2
[0,3,0] → 3
```

**Constraints**
* `1 <= n <= 100`

## Approach: Post-order surplus

> Every edge must carry the surplus (or deficit) of the subtree below it; the answer is the sum of |surplus| over all edges.

**Edge flow.** A subtree with `s` nodes and `c` coins has surplus `c - s`. Exactly `|c - s|` coins must cross the edge above it (out if
positive, in if negative), and that is achievable. A post-order walk returns `node.val - 1 + left + right`, adding `|left| + |right|` to
the move count.

* Time: **O(n)**.
* Space: **O(h)** — recursion depth.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0979/v1/DistributeCoins.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0979/v1/DistributeCoinsTest.java` | JUnit 6 tests |
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
