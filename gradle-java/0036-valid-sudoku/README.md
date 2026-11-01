# 36. Valid Sudoku

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Matrix &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/valid-sudoku/)

## Problem

Decide whether a partially filled 9×9 Sudoku board is **valid**. Only the filled cells need to follow the rules:
* each row has the digits `1-9` at most once,
* each column has the digits `1-9` at most once,
* each of the nine 3×3 boxes has the digits `1-9` at most once.

Empty cells are `'.'`. A valid board does not need to be solvable.

**Example**
```
Input: the classic example board (rows "53..7....", "6..195...", ...)
Output: true
Changing the top-left 5 to 8 makes column 0 contain 8 twice → false
```

**Constraints**
* `board` is 9×9; each cell is a digit `1-9` or `'.'`.

## Solutions

One solution, in subproject `v1`.

| Version | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1](v1/README.md) | Seen sets in one pass | `O(1)` | `O(1)` | [▶ animation](v1/animation/index.html) |

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
