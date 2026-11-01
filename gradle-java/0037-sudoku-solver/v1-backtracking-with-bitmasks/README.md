# 37. Sudoku Solver — v1: Backtracking with bitmasks

**Difficulty:** Hard &nbsp;|&nbsp; **Topic:** Backtracking &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/sudoku-solver/)

## Problem

Fill the empty cells (`'.'`) of a 9×9 Sudoku so that every row, column and 3×3 box contains `1-9` exactly once. The input has exactly
one solution; modify `board` in place.

**Constraints**
* `board` is 9×9; the puzzle has exactly one solution.

## Approach: Backtracking with bitmasks

> Fill empty cells one by one with digits allowed by row, column and box masks; undo on dead ends.

**Backtracking + bitmasks.** Keep a 9-bit mask of used digits per row, column and box. Collect the empty cells; `solve(k)` tries each
digit free in all three masks for cell `k`, recurses, and undoes on failure.

* Time: **O(9^E)** — E empty cells in the worst case (much faster in practice thanks to pruning).
* Space: **O(E)** — the recursion depth.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0037/v1/SudokuSolver.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0037/v1/SudokuSolverTest.java` | JUnit 6 tests |
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
