# 637. Average of Levels in Binary Tree — v1: Level-order BFS

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Binary Tree BFS &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/average-of-levels-in-binary-tree/)

## Problem

Return the average value of the nodes on each level of a binary tree, from top to bottom. Answers within `10^-5` are accepted.

**Example**
```
Input:  [3,9,20,null,null,15,7]
Output: [3.00000,14.50000,11.00000]
```

**Constraints**
* `1 <= n <= 10^4`; `-2^31 <= Node.val <= 2^31 - 1`

## Approach: Level-order BFS

> Sum each level during a level-order traversal and divide by its size.

**BFS by levels.** Pop exactly one level at a time, summing values in a `long` (to avoid overflow), and divide by the level size.

* Time: **O(n)** — each node is enqueued once.
* Space: **O(w)** — the widest level.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0637/v1/AverageOfLevels.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0637/v1/AverageOfLevelsTest.java` | JUnit 6 tests |
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
