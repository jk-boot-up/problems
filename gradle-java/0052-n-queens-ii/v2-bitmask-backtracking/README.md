# 52. N-Queens II — v2: Bitmask backtracking

**Difficulty:** Hard &nbsp;|&nbsp; **Topic:** Backtracking &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/n-queens-ii/)

## Problem

Place `n` queens on an `n × n` chessboard so that no two attack each other (no shared row, column or diagonal). Return the number of
distinct solutions.

**Example**
```
Input:  n = 4
Output: 2
```

**Constraints**
* `1 <= n <= 9`

## Approach: Bitmask backtracking

> Place one queen per row; three bitmasks track attacked columns and both diagonals.

**Bitmasks.** Go row by row. `cols`, `diag1` and `diag2` mark attacked squares for the current row (the diagonal masks shift by one
column per row). Free squares are `~(cols | diag1 | diag2) & full`; take the lowest free bit, recurse, repeat.

* Time: **O(n!)** — at most n choices in row 0, n − 1 in row 1, and so on (far fewer after pruning).
* Space: **O(n)** — the recursion depth.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0052/v2/NQueensII.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0052/v2/NQueensIITest.java` | JUnit 6 tests |
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

* [v1-boolean-arrays](../v1-boolean-arrays/README.md): Boolean arrays (`O(n!)` time, `O(n)` space)
