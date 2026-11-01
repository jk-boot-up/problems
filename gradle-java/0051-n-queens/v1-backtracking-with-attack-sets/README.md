# 51. N-Queens — v1: Backtracking with attack sets

**Difficulty:** Hard &nbsp;|&nbsp; **Topic:** Backtracking &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/n-queens/)

## Problem

Return all distinct solutions to the `n`-queens puzzle as boards of strings, where `'Q'` is a queen and `'.'` an empty square.

**Example**
```
n = 4 → [[".Q..","...Q","Q...","..Q."], ["..Q.","Q...","...Q",".Q.."]]
```

**Constraints**
* `1 <= n <= 9`

## Approach: Backtracking with attack sets

> Row by row, place a queen in a column not attacked by column or either diagonal; record full boards.

**Backtracking.** Row by row, try each column whose `col[c]`, `d1[r + c]` and `d2[r - c + n - 1]` flags are free. When all rows are
filled, build the board strings.

* Time: **O(n!)** — at most n choices in the first row, n − 1 in the next, and so on.
* Space: **O(n)** — the flags and current placement (plus the output).

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0051/v1/NQueens.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0051/v1/NQueensTest.java` | JUnit 6 tests |
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
