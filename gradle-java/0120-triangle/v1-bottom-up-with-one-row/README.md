# 120. Triangle — v1: Bottom-up with one row

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Multidimensional DP &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/triangle/)

## Problem

Given a `triangle` of numbers, return the minimum path sum from top to bottom. From row `i`, index `j`, you may move to index `j` or
`j + 1` of the next row.

**Example**
```
   2
  3 4
 6 5 7
4 1 8 3
Output: 11   (2 + 3 + 5 + 1)
```

**Constraints**
* `1 <= triangle.length <= 200`

**Follow-up:** O(n) extra space, n = number of rows.

## Approach: Bottom-up with one row

> Work from the bottom row up: each cell adds the cheaper of the two cells below it.

**Bottom-up.** Copy the last row into `best`. For each row going up, `best[j] = row[j] + min(best[j], best[j + 1])`. Then `best[0]` is the answer.

* Time: **O(n²)** — every cell is processed once.
* Space: **O(n)** — one row of partial sums.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0120/v1/Triangle.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0120/v1/TriangleTest.java` | JUnit 6 tests |
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
