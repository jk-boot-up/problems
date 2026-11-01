# 329. Longest Increasing Path in a Matrix — v1: Memoized DFS

**Difficulty:** Hard &nbsp;|&nbsp; **Topic:** Graph General &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/longest-increasing-path-in-a-matrix/)

## Problem

Return the length of the longest strictly increasing path in an integer matrix, moving up, down, left or right.

**Example**
```
[[9,9,4],[6,6,8],[2,1,1]] → 4   (1 → 2 → 6 → 9)
```

**Constraints**
* `1 <= m, n <= 200`

## Approach: Memoized DFS

> DFS from each cell with memoization: the longest path from a cell is 1 + the best path from a larger neighbour.

**Memo DFS.** `len(r, c) = 1 + max(len(neighbour))` over neighbours with a larger value. Strictly increasing paths cannot cycle, so the
memo is safe; each cell is computed once.

* Time: **O(m·n)** — each cell computed once, four neighbours each.
* Space: **O(m·n)** — the memo and the recursion depth.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0329/v1/LongestIncreasingPath.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0329/v1/LongestIncreasingPathTest.java` | JUnit 6 tests |
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
