# 119. Pascal's Triangle II — v1: One row, updated right to left

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** 1D DP &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/pascals-triangle-ii/)

## Problem

Return row `rowIndex` (0-based) of Pascal's triangle.

**Example**
```
3 → [1,3,3,1],   0 → [1],   1 → [1,1]
```

**Constraints**
* `0 <= rowIndex <= 33`

**Follow-up:** O(rowIndex) extra space.

## Approach: One row, updated right to left

> Update one row in place from right to left: row[j] += row[j − 1].

**In-place update.** Start with `[1]`. For each new row, append 1 and update `j` from right to left with `row[j] += row[j-1]`, so each
update still reads the previous row's values.

* Time: **O(k²)** — k rows of up to k updates.
* Space: **O(k)** — the single row.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0119/v1/PascalsTriangleII.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0119/v1/PascalsTriangleIITest.java` | JUnit 6 tests |
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
