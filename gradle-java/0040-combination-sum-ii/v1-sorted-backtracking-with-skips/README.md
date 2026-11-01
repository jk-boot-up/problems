# 40. Combination Sum II — v1: Sorted backtracking with skips

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Backtracking &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/combination-sum-ii/)

## Problem

Find all unique combinations of `candidates` that sum to `target`. Each candidate may be used **once**; the input may contain duplicates,
but the output must not contain duplicate combinations.

**Example**
```
candidates = [10,1,2,7,6,1,5], target = 8 → [[1,1,6],[1,2,5],[1,7],[2,6]]
```

**Constraints**
* `1 <= candidates.length <= 100`; `1 <= target <= 30`

## Approach: Sorted backtracking with skips

> Sorted backtracking where each candidate is used once and equal candidates are skipped at the same depth.

**Backtracking.** Sort. At each depth iterate `i >= start`, skip `nums[i] == nums[i-1]` when `i > start`, stop once `nums[i] > remaining`,
and recurse with `i + 1` (no reuse).

* Time: **O(2ⁿ · n)** — worst case explores every subset.
* Space: **O(n)** — the recursion depth.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0040/v1/CombinationSumII.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0040/v1/CombinationSumIITest.java` | JUnit 6 tests |
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
