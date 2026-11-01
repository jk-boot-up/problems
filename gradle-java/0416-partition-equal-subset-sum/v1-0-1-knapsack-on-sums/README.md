# 416. Partition Equal Subset Sum — v1: 0/1 knapsack on sums

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** 1D DP &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/partition-equal-subset-sum/)

## Problem

Return `true` if `nums` can be split into two subsets with equal sums.

**Example**
```
[1,5,11,5] → true ([1,5,5] and [11]),   [1,2,3,5] → false
```

**Constraints**
* `1 <= nums.length <= 200`; `1 <= nums[i] <= 100`

## Approach: 0/1 knapsack on sums

> Can some subset reach half of the total? A boolean knapsack over sums answers that.

**Subset sum.** If the total is odd, it is impossible. Otherwise `can[s]` says whether some subset sums to `s`; for each number `x`, update
`s` from `target` down to `x`: `can[s] |= can[s - x]` (going down uses each number once).

* Time: **O(n · S)** — S is half the total.
* Space: **O(S)** — one boolean array.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0416/v1/PartitionEqualSubsetSum.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0416/v1/PartitionEqualSubsetSumTest.java` | JUnit 6 tests |
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
