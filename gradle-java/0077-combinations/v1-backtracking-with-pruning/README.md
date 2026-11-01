# 77. Combinations — v1: Backtracking with pruning

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Backtracking &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/combinations/)

## Problem

Return all combinations of `k` numbers chosen from `1..n`, in any order.

**Example**
```
Input:  n = 4, k = 2
Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
```

**Constraints**
* `1 <= n <= 20`; `1 <= k <= n`

## Approach: Backtracking with pruning

> Choose numbers in increasing order so each set is built exactly once; stop early when too few numbers remain.

**Increasing choices.** `backtrack(start)`: if the path has `k` numbers, record it. Otherwise try each `i` from `start` up to
`n - (k - path.size()) + 1` (later starts could not fill the remaining slots), push `i`, recurse with `i + 1`, pop.

* Time: **O(C(n, k) · k)** — one copy of length k per combination.
* Space: **O(k)** — the recursion depth and path.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0077/v1/Combinations.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0077/v1/CombinationsTest.java` | JUnit 6 tests |
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
