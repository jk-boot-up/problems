# 1254. Number of Closed Islands — v1: Sink border islands, then count

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Graph DFS &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/number-of-closed-islands/)

## Problem

In this grid **`0` is land** and `1` is water. An island is a 4-connected group of `0`s; it is **closed** if it is completely surrounded
by water (it does not touch the grid border). Return the number of closed islands.

**Example**
```
1 1 1 1 1 1 1 0
1 0 0 0 0 1 1 0
1 0 1 0 1 1 1 0      → 2
1 0 0 0 0 1 0 1
1 1 1 1 1 1 1 0
```

**Constraints**
* `1 <= rows, cols <= 100`

## Approach: Sink border islands, then count

> Remove islands that touch the border, then count the islands that remain.

**Two flood fills.** First sink (turn into water) every island reachable from a border land cell; those are not closed. Then every
remaining island is closed: count them, sinking each as it is found. Work on a copy so the input is untouched.

* Time: **O(mn)**.
* Space: **O(mn)** — the copy and the fill stack.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p1254/v1/NumberOfClosedIslands.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p1254/v1/NumberOfClosedIslandsTest.java` | JUnit 6 tests |
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
