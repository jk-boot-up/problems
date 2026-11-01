# 289. Game of Life

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

## Solutions

Each version is a separate Gradle subproject, ordered from the simplest idea to the most efficient one.

| Version | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1](v1/README.md) | Copy of the board | `O(m·n)` | `O(m·n)` | [▶ animation](v1/animation/index.html) |
| [v2](v2/README.md) | In-place two-bit states | `O(m·n)` | `O(1)` | [▶ animation](v2/animation/index.html) |

## Build and test

Only a JDK is needed to start Gradle; JDK 25 is downloaded automatically if it is missing.

```bash
./gradlew test          # every version
./gradlew :v1:test      # one version
```

## Animation

Open `vN/animation/index.html` in a browser. It has three tabs:

* **Problem:** the statement and the key idea.
* **Walkthrough:** pick a scenario and press **Play**. Each step is animated and read aloud by your browser's speech engine
  (untick *Narration* to mute). Keys: space = play/pause, ← / → = step, 1–9 = scenario.
* **Complexity:** time and space cost, plotted against the common growth curves, and compared across versions.

Use the header to switch between Light, Medium and Dark themes and between solution versions.
