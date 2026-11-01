# 39. Combination Sum — v1: Sorted backtracking

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Backtracking &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/combination-sum/)

## Problem

Given **distinct** positive `candidates` and a `target`, return all unique combinations whose sum is `target`. Each candidate may be
used **any number of times**. Two combinations are different if some number is used a different number of times.

**Example**
```
Input:  candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
```

**Constraints**
* `1 <= candidates.length <= 30`; `2 <= candidates[i] <= 40`; `1 <= target <= 40`

## Approach: Sorted backtracking

> Try candidates in sorted order, allowing reuse; stop a branch as soon as a candidate exceeds what remains.

**Backtracking from a start index.** Sort the candidates. `bt(start, remaining)`: if `remaining == 0`, record the path. Otherwise for
`i >= start`, break once `candidates[i] > remaining`; else push it and recurse with the **same** `i` (reuse allowed).

* Time: **O(N^(T/M))** — roughly, with T the target and M the smallest candidate (the depth of the search tree).
* Space: **O(T/M)** — the recursion depth.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0039/v1/CombinationSum.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0039/v1/CombinationSumTest.java` | JUnit 6 tests |
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
