# 1337. The K Weakest Rows in a Matrix — v1: Binary search counts + sort

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Binary Search &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix/)

## Problem

Each row of a binary matrix has its soldiers (`1`) before its civilians (`0`). Row `i` is weaker than row `j` if it has fewer soldiers,
or the same number and `i < j`. Return the indices of the `k` weakest rows, weakest first.

**Example**
```
[[1,1,0,0,0],
 [1,1,1,1,0],
 [1,0,0,0,0],
 [1,1,0,0,0],
 [1,1,1,1,1]], k = 3 → [2,0,3]
```

**Constraints**
* `2 <= m, n <= 100`, `1 <= k <= m`

## Approach: Binary search counts + sort

> Soldiers (1s) come first in each row, so binary search counts them; then sort rows by (count, index).

**Count, then order.** Binary search each row for the first `0`; its index is the soldier count. Encode each row as `count * m + index`
so a plain integer sort orders by count, then by index, and take the first `k`.

* Time: **O(m log n + m log m)**.
* Space: **O(m)**.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p1337/v1/KWeakestRows.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p1337/v1/KWeakestRowsTest.java` | JUnit 6 tests |
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
