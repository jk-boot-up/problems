# 561. Array Partition — v1: Sort and take every other

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Greedy &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/array-partition/)

## Problem

Group `2n` integers into `n` pairs to maximize the sum of `min(a, b)` over all pairs. Return that sum.

**Example**
```
[1,4,3,2] → 4 ((1,2), (3,4)),   [6,2,6,5,1,2] → 9
```

**Constraints**
* `1 <= n <= 10^4`

## Approach: Sort and take every other

> Sort and pair neighbours; the sum of every other element (the smaller of each pair) is maximal.

**Pair neighbours after sorting.** The smallest element is a minimum anyway, so pair it with the next smallest to waste as little as possible;
repeat. The answer is the sum of elements at even indices of the sorted array.

* Time: **O(n log n)** — sorting.
* Space: **O(log n)** — the sort's stack.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0561/v1/ArrayPartition.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0561/v1/ArrayPartitionTest.java` | JUnit 6 tests |
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
