# 494. Target Sum — v1: Subset-count DP

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** 1D DP &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/target-sum/)

## Problem

Put `+` or `-` in front of every number of `nums` so the expression evaluates to `target`. Return the number of ways.

**Example**
```
nums = [1,1,1,1,1], target = 3 → 5
nums = [1], target = 1          → 1
```

**Constraints**
* `1 <= nums.length <= 20`; `0 <= nums[i] <= 1000`; `-1000 <= target <= 1000`

## Approach: Subset-count DP

> Choosing a plus-set P: sum(P) = (total + target) / 2, so count subsets with that sum.

**Reduce to subset counting.** With `P` the numbers given `+`: `sum(P) - (total - sum(P)) = target`, so `sum(P) = (total + target) / 2`.
If that is negative or not an integer, there are 0 ways. Otherwise `ways[s] += ways[s - x]` for each `x`, iterating `s` downward.

* Time: **O(n · S)** — S = (total + target) / 2.
* Space: **O(S)** — one array.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0494/v1/TargetSum.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0494/v1/TargetSumTest.java` | JUnit 6 tests |
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
