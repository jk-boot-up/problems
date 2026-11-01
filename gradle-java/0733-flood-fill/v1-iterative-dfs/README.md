# 733. Flood Fill — v1: Iterative DFS

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Graph General &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/flood-fill/)

## Problem

Starting from pixel `(sr, sc)`, repaint it and every 4-directionally connected pixel of the same original colour with `color`. Return the image.

**Example**
```
image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, color = 2 → [[2,2,2],[2,2,0],[2,0,1]]
```

**Constraints**
* `1 <= m, n <= 50`

## Approach: Iterative DFS

> DFS from the start pixel, repainting every connected pixel that has the original colour.

**DFS with a stack.** If the start already has the new colour, nothing changes (and we avoid looping). Otherwise paint pixels as they are
pushed and spread to same-coloured neighbours.

* Time: **O(m·n)** — each pixel at most once.
* Space: **O(m·n)** — the stack.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0733/v1/FloodFill.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0733/v1/FloodFillTest.java` | JUnit 6 tests |
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
