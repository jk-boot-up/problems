# 130. Surrounded Regions — v1: Flood fill from the border

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Graph General &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/surrounded-regions/)

## Problem

Given an `m × n` board of `'X'` and `'O'`, capture every region of `'O'` that is **completely surrounded** by `'X'` (connected
horizontally or vertically) by flipping it to `'X'`. Regions touching the border are not surrounded.

**Example**
```
Input:          Output:
X X X X         X X X X
X O O X         X X X X
X X O X         X X X X
X O X X         X O X X
```

**Constraints**
* `1 <= m, n <= 200`

## Approach: Flood fill from the border

> Only O regions touching the border survive; mark them from the border, then flip everything else.

**Think in reverse.** Flood fill from every border `'O'` and mark its region as safe (`'#'`). Then scan: remaining `'O'` cells are
surrounded, so flip them to `'X'`; turn `'#'` back into `'O'`.

* Time: **O(m·n)** — each cell is visited a constant number of times.
* Space: **O(m·n)** — the flood-fill stack in the worst case.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0130/v1/SurroundedRegions.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0130/v1/SurroundedRegionsTest.java` | JUnit 6 tests |
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
