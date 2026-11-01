# 1926. Nearest Exit from Entrance in Maze — v1: BFS from the entrance

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Graph BFS &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/nearest-exit-from-entrance-in-maze/)

## Problem

In a maze of `'.'` (empty) and `'+'` (wall), starting at `entrance`, return the number of steps to the nearest **exit**: an empty cell on the
border that is not the entrance. Return `-1` if none is reachable.

**Example**
```
maze = [["+","+",".","+"],[".",".",".","+"],["+","+","+","."]], entrance = [1,2] → 1
maze = [["+","+","+"],[".",".","."],["+","+","+"]], entrance = [1,0]             → 2
```

**Constraints**
* `1 <= m, n <= 100`

## Approach: BFS from the entrance

> BFS from the entrance; the first empty border cell reached (other than the entrance) is the nearest exit.

**Level-order BFS.** Mark cells as visited when enqueued. Each level is one step; the first border cell dequeued (excluding the start)
is the answer.

* Time: **O(m·n)** — each cell once.
* Space: **O(m·n)** — the queue and marks.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p1926/v1/NearestExit.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p1926/v1/NearestExitTest.java` | JUnit 6 tests |
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
