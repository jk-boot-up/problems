# 378. Kth Smallest Element in a Sorted Matrix — v1: Min-heap over rows

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

## Approach: Min-heap over rows

> Merge the sorted rows with a heap and pop k times.

**k-way merge.** Push the first element of each row. Pop the smallest `k` times; after each pop, push the next element of the same row.
The `k`-th pop is the answer.

* Time: **O(k log n)** — `k` pops from a heap of at most `n` entries.
* Space: **O(n)** — the heap.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0378/v1/KthSmallestInMatrix.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0378/v1/KthSmallestInMatrixTest.java` | JUnit 6 tests |
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

* [v2-binary-search-on-value](../v2-binary-search-on-value/README.md): Binary search on value (`O(n log R)` time, `O(1)` space)
