# 289. Game of Life — v2: In-place two-bit states

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

## Approach: In-place two-bit states

> Update in place by encoding both the old and new state in each cell (bit 0 = now, bit 1 = next).

**Two bits per cell.** Bit 0 is the current state, bit 1 the next state. Count live neighbours using `cell & 1`, so cells
already updated still report their old state. Set bit 1 when the cell lives next round. Finally shift every cell right by one.

* Time: **O(m·n)** — 8 neighbour checks per cell.
* Space: **O(1)** — the board stores both generations.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0289/v2/GameOfLife.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0289/v2/GameOfLifeTest.java` | JUnit 6 tests |
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

* [v1-copy-of-the-board](../v1-copy-of-the-board/README.md): Copy of the board (`O(m·n)` time, `O(m·n)` space)
