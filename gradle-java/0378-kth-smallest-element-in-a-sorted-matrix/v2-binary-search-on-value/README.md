# 378. Kth Smallest Element in a Sorted Matrix — v2: Binary search on value

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Binary Search &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/)

## Problem

In an `n × n` matrix where every row and every column is sorted ascending, return the `k`-th smallest element (counting duplicates).

**Example**
```
matrix = [[1,5,9],[10,11,13],[12,13,15]], k = 8 → 13
matrix = [[-5]], k = 1 → -5
```

**Constraints**
* `1 <= n <= 300`, `-10^9 <= matrix[i][j] <= 10^9`, `1 <= k <= n²`

## Approach: Binary search on value

> Binary search on the value; count entries ≤ mid with a staircase walk from the bottom-left corner.

**Search values, not positions.** The answer lies in `[matrix[0][0], matrix[n-1][n-1]]`. For a guess `mid`, count entries `<= mid`:
start at the bottom-left; if the entry is `<= mid`, the whole column above it is too (add `row + 1`, move right), otherwise move up. If
the count is less than `k`, the answer is bigger; otherwise it is `mid` or smaller. The range always ends on a value in the matrix. Use
`long` so `lo + hi` cannot overflow.

* Time: **O(n log R)** — `R` is the value range; each count is O(n).
* Space: **O(1)**.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0378/v2/KthSmallestInMatrix.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0378/v2/KthSmallestInMatrixTest.java` | JUnit 6 tests |
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

* [v1-min-heap-over-rows](../v1-min-heap-over-rows/README.md): Min-heap over rows (`O(k log n)` time, `O(n)` space)
