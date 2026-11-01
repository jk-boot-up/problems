# 289. Game of Life — v1: Copy of the board

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Matrix &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/game-of-life/)

## Problem

The board is an `m × n` grid of cells, each live (`1`) or dead (`0`). Each cell looks at its 8 neighbours and, **all at the
same time**:
1. a live cell with fewer than 2 live neighbours dies;
2. a live cell with 2 or 3 live neighbours lives on;
3. a live cell with more than 3 live neighbours dies;
4. a dead cell with exactly 3 live neighbours becomes live.

Update `board` in place to the next state.

**Example**
```
Input:  [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
Output: [[0,0,0],[1,0,1],[0,1,1],[0,1,0]]
```

**Constraints**
* `1 <= m, n <= 25`

**Follow-up:** solve it in place.

## Approach: Copy of the board

> Read neighbours from an untouched copy and write the new states into the board.

**Snapshot.** Copy the board; count neighbours in the copy and write each cell's next state into the original.

* Time: **O(m·n)** — 8 neighbour checks per cell.
* Space: **O(m·n)** — the copy.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0289/v1/GameOfLife.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0289/v1/GameOfLifeTest.java` | JUnit 6 tests |
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
* **Complexity:** time and space cost, plotted against the common growth curves, and compared with the other approaches.

Switch between Light, Medium and Dark themes in the header.

## Other approaches

* [v2-in-place-two-bit-states](../v2-in-place-two-bit-states/README.md): In-place two-bit states (`O(m·n)` time, `O(1)` space)
