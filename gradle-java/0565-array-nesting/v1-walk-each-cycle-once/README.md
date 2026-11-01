# 565. Array Nesting — v1: Walk each cycle once

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Array &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/array-nesting/)

## Problem

`nums` is a permutation of `0..n-1`. Starting at `k`, build `s[k] = {nums[k], nums[nums[k]], …}` until a value repeats. Return the size of
the largest `s[k]`.

**Example**
```
[5,4,0,3,1,6,2] → 4   (0 → 5 → 6 → 2 → 0)
[0,1,2]         → 1
```

**Constraints**
* `1 <= nums.length <= 10^5`

## Approach: Walk each cycle once

> A permutation splits into cycles; the answer is the longest cycle, and each cycle needs to be walked only once.

**Cycles.** Following `i → nums[i]` in a permutation always returns to the start, and every starting point on the same cycle gives the same
set. Walk each cycle from its first unvisited index, marking indices as visited (by writing `-1`, on a copy), and keep the longest length.

* Time: **O(n)** — every index is visited once.
* Space: **O(n)** — the copy (O(1) if the input may be modified).

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0565/v1/ArrayNesting.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0565/v1/ArrayNestingTest.java` | JUnit 6 tests |
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
