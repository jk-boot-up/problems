# 515. Find Largest Value in Each Tree Row — v1: BFS with a level maximum

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Binary Tree BFS &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/find-largest-value-in-each-tree-row/)

## Problem

Return the largest value in each row of a binary tree, from top to bottom.

**Example**
```
[1,3,2,5,3,null,9] → [1,3,9]
[1,2,3]            → [1,3]
```

**Constraints**
* `0 <= n <= 10^4`

## Approach: BFS with a level maximum

> Level-order traversal, keeping the maximum of each level.

**Level by level.** Process the queue one level at a time (its size at the start of the level) and track the maximum.

* Time: **O(n)**.
* Space: **O(w)** — the widest level.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0515/v1/LargestValuePerRow.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0515/v1/LargestValuePerRowTest.java` | JUnit 6 tests |
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
