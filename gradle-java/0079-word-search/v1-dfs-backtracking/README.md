# 79. Word Search — v1: DFS backtracking

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Backtracking &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/word-search/)

## Problem

Given an `m × n` grid of letters and a `word`, return `true` if the word can be traced through **adjacent** cells (horizontally or
vertically), using each cell at most once.

**Example**
```
Input:  board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
        word = "ABCCED" → true,  "SEE" → true,  "ABCB" → false
```

**Constraints**
* `1 <= m, n <= 6`; `1 <= word.length <= 15`

## Approach: DFS backtracking

> DFS from every cell, matching one letter per step and marking cells as used along the current path.

**Backtracking.** Try each cell as the start. `dfs(r, c, i)` fails if out of bounds or the letter differs from `word[i]`; otherwise
mark the cell (`'#'`), try the four neighbours for `i + 1`, then restore the letter.

* Time: **O(m·n·3^L)** — each start explores up to 3 new directions per letter (the cell it came from is used).
* Space: **O(L)** — the recursion depth.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0079/v1/WordSearch.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0079/v1/WordSearchTest.java` | JUnit 6 tests |
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
