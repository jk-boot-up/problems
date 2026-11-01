# 1498. Number of Subsequences That Satisfy the Given Sum Condition — v1: Sort, two pointers, powers of two

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Two Pointers &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/number-of-subsequences-that-satisfy-the-given-sum-condition/)

## Problem

Count the non-empty subsequences of `nums` whose `min + max <= target`. Return the count modulo `10^9 + 7`.

**Example**
```
nums = [3,5,6,7],     target = 9  → 4    ([3], [3,5], [3,5,6], [3,6])
nums = [3,3,6,8],     target = 10 → 6
nums = [2,3,3,4,6,7], target = 12 → 61
```

**Constraints**
* `1 <= nums.length <= 10^5`, `1 <= nums[i], target <= 10^6`

## Approach: Sort, two pointers, powers of two

> After sorting, only the min and max matter; fixing the min, any subset of elements up to the farthest valid max works.

**Fix the minimum.** A subsequence's min and max do not depend on order, so sort. With `lo` as the minimum, move `hi` left until
`nums[lo] + nums[hi] <= target`. Then every subset of `nums[lo+1..hi]` combined with `nums[lo]` is valid: `2^(hi - lo)` of them. If the
pair fails, `nums[hi]` is too big for every later minimum too, so drop it. Precompute powers of two mod `10^9 + 7`.

* Time: **O(n log n)** — sorting.
* Space: **O(n)** — the powers.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p1498/v1/NumSubseqSumCondition.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p1498/v1/NumSubseqSumConditionTest.java` | JUnit 6 tests |
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
