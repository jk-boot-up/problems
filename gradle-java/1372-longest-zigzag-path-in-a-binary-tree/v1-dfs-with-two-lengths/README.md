# 1372. Longest ZigZag Path in a Binary Tree — v1: DFS with two lengths

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Binary Tree General &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/longest-zigzag-path-in-a-binary-tree/)

## Problem

A zigzag path alternates between left and right child moves. Its length is the number of edges. Return the longest zigzag path in the tree.

**Example**
```
[1,null,1,1,1,null,null,1,1,null,1,null,null,null,1] → 3
[1,1,1,null,1,null,null,1,1,null,1]                  → 4
```

**Constraints**
* `1 <= n <= 5 * 10^4`

## Approach: DFS with two lengths

> Each node knows the zigzag length arriving from the left and from the right; turning extends, going straight restarts.

**Carry both directions.** `dfs(node, leftLen, rightLen)`: `leftLen` is the zigzag length if the last move was to the left (so the next
must go right). Going left continues `rightLen + 1` and resets the other to 0; going right continues `leftLen + 1`.

* Time: **O(n)** — each node once.
* Space: **O(h)** — the recursion stack.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p1372/v1/LongestZigZag.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p1372/v1/LongestZigZagTest.java` | JUnit 6 tests |
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
