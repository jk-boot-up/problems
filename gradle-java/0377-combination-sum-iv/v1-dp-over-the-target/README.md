# 377. Combination Sum IV — v1: DP over the target

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Dynamic Programming &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/combination-sum-iv/)

## Problem

Given distinct positive integers `nums` and a `target`, return the number of **ordered** sequences of numbers from `nums` (repeats allowed)
that add up to `target`. The answer fits in a 32-bit integer.

**Example**
```
nums = [1,2,3], target = 4 → 7
   (1,1,1,1) (1,1,2) (1,2,1) (1,3) (2,1,1) (2,2) (3,1)
nums = [9], target = 3 → 0
```

**Constraints**
* `1 <= nums.length <= 200`, `1 <= nums[i], target <= 1000`

## Approach: DP over the target

> Order matters, so ways(t) sums ways(t − x) over every choice x of the last number.

**Last element.** `ways[0] = 1` (the empty sequence). For `t = 1..target`, every sequence summing to `t` ends in some `x`, so
`ways[t] = Σ ways[t - x]` over `x <= t`. Some unused intermediate values can overflow an `int`; Java's wrap-around arithmetic is exact
modulo `2^32`, so the guaranteed-small final answer is still correct.

* Time: **O(target · n)**.
* Space: **O(target)**.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0377/v1/CombinationSumIV.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0377/v1/CombinationSumIVTest.java` | JUnit 6 tests |
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
