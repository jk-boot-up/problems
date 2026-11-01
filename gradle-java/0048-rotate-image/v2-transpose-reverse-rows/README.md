# 48. Rotate Image — v2: Transpose + reverse rows

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Matrix &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/rotate-image/)

## Problem

Rotate an `n × n` matrix by 90 degrees **clockwise**, **in place** (do not allocate another matrix).

**Example 1**
```
Input:  [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]
```

**Example 2**
```
Input:  [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
```

**Constraints**
* `1 <= n <= 20`, `-1000 <= matrix[i][j] <= 1000`

## Approach: Transpose + reverse rows

> A clockwise rotation equals a transpose followed by reversing every row.

**Transpose, then mirror.** Swap `a[i][j]` with `a[j][i]` for `j > i` (transpose), then reverse each row.
Element `(i, j)` ends at `(j, n-1-i)`, which is exactly the clockwise rotation.

* Time: **O(n²)** — every cell is swapped a constant number of times.
* Space: **O(1)** — swaps in place.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0048/v2/RotateImage.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0048/v2/RotateImageTest.java` | JUnit 6 tests |
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
  engine (untick *Narration* to mute). Keys: space = play/pause, ← / → = step, 1–9 = scenario.
* **Complexity:** time and space cost, plotted against the common growth curves, and compared with the other approaches.

Switch between Light, Medium and Dark themes in the header.

## Other approaches

* [v1-copy-into-a-new-matrix](../v1-copy-into-a-new-matrix/README.md): Copy into a new matrix (`O(n²)` time, `O(n²)` space)
