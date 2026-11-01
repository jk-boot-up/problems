# 502. IPO — v1: Sort by capital + max-heap of profits

**Difficulty:** Hard &nbsp;|&nbsp; **Topic:** Heap &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/ipo/)

## Problem

You have initial capital `w` and may finish at most `k` distinct projects. Project `i` needs at least `capital[i]` to start and adds
`profits[i]` to your capital when finished. Return the maximum capital after at most `k` projects.

**Example**
```
Input:  k = 2, w = 0, profits = [1,2,3], capital = [0,1,1]
Output: 4   (do project 0 → w = 1, then project 2 → w = 4)
```

**Constraints**
* `1 <= k <= 10^5`; `0 <= w <= 10^9`; `1 <= n <= 10^5`

## Approach: Sort by capital + max-heap of profits

> Unlock every project you can afford, then always take the most profitable unlocked one.

**Greedy with two structures.** Sort projects by required capital. Repeat `k` times: push the profits of every project whose capital
requirement is now within `w` into a max-heap; if the heap is empty, stop; otherwise add the largest profit to `w`.

* Time: **O(n log n)** — sorting plus heap operations (k ≤ n relevant pops).
* Space: **O(n)** — the sorted index and the heap.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0502/v1/IPO.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0502/v1/IPOTest.java` | JUnit 6 tests |
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
