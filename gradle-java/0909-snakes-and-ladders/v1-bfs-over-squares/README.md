# 909. Snakes and Ladders — v1: BFS over squares

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Graph BFS &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/snakes-and-ladders/)

## Problem

An `n × n` board is numbered `1..n²` in a **boustrophedon** pattern starting at the bottom-left (row direction alternates). From
square `cur`, a die roll moves you to any of `cur+1 .. min(cur+6, n²)`. If that square has `board[r][c] != -1`, you must take the
snake or ladder to that square (only one per move). Return the fewest rolls to reach `n²`, or `-1`.

**Example**
```
Input:  board = [[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],
                 [-1,35,-1,-1,13,-1],[-1,-1,-1,-1,-1,-1],[-1,15,-1,-1,-1,-1]]
Output: 4
```

**Constraints**
* `2 <= n <= 20`; squares 1 and n² have no snake or ladder.

## Approach: BFS over squares

> Each square is a node with edges to the next six squares (after following a snake or ladder); BFS finds the fewest rolls.

**BFS.** Convert a square number to `(row, col)`: `row = n - 1 - (s - 1) / n`, `col = (s - 1) % n`, mirrored on every other row.
BFS from square 1; neighbours are the next six squares after following any snake or ladder. The first time `n²` is dequeued gives the
minimum number of rolls.

* Time: **O(n²)** — each square is visited once with six edges.
* Space: **O(n²)** — the distance array.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0909/v1/SnakesAndLadders.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0909/v1/SnakesAndLaddersTest.java` | JUnit 6 tests |
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
